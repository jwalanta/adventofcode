package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func countNeighbors(l [100][100]bool, row, col int) int {
	count := 0
	for r := row - 1; r <= row+1; r++ {
		for c := col - 1; c <= col+1; c++ {
			if r < 0 || c < 0 || r > 99 || c > 99 || (r == row && c == col) {
				continue
			}
			if l[r][c] {
				count++
			}
		}
	}
	return count
}

func animate(light [100][100]bool) [100][100]bool {
	l := [100][100]bool{}

	for r := 0; r < 100; r++ {
		for c := 0; c < 100; c++ {
			count := countNeighbors(light, r, c)

			// A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
			// A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
			if light[r][c] {
				if count == 2 || count == 3 {
					l[r][c] = true
				}
			} else {
				if count == 3 {
					l[r][c] = true
				}
			}
		}
	}

	return l
}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	//
	// part 1
	//
	light := [100][100]bool{}

	for r := 0; r < 100; r++ {
		for c := 0; c < 100; c++ {
			if lines[r][c] == '#' {
				light[r][c] = true
			}
		}
	}

	for s := 0; s < 100; s++ {
		light = animate(light)
	}

	count := 0

	for r := 0; r < 100; r++ {
		for c := 0; c < 100; c++ {
			if light[r][c] {
				count++
			}
		}
	}

	fmt.Println("part 1:", count)

	//
	// part 2
	//
	for r := 0; r < 100; r++ {
		for c := 0; c < 100; c++ {
			if lines[r][c] == '#' {
				light[r][c] = true
			} else {
				light[r][c] = false
			}
		}
	}

	for s := 0; s < 100; s++ {
		light = animate(light)

		// lights at corners cant turn off
		light[0][0] = true
		light[0][99] = true
		light[99][0] = true
		light[99][99] = true
	}

	count = 0

	for r := 0; r < 100; r++ {
		for c := 0; c < 100; c++ {
			if light[r][c] {
				count++
			}
		}
	}

	fmt.Println("part 2:", count)

}
