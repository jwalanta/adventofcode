package main

import (
	"fmt"
	"io/ioutil"
)

type Coord struct {
	x, y int
}

func part1(str string) int {

	houses := make(map[Coord]int)

	x, y := 0, 0

	houses[Coord{x, y}] = 1

	for _, s := range str {
		if s == '^' {
			y--
		}
		if s == 'v' {
			y++
		}
		if s == '<' {
			x--
		}
		if s == '>' {
			x++
		}

		houses[Coord{x, y}]++
	}

	count := 0
	for _, n := range houses {

		if n >= 1 {
			count++
		}
	}

	fmt.Println(count)
	return count
}

func part2(str string) int {

	houses := make(map[Coord]int)

	sx, sy := 0, 0
	rx, ry := 0, 0

	houses[Coord{sx, sy}] = 2

	santasTurn := true

	for _, s := range str {

		if santasTurn {
			if s == '^' {
				sy--
			}
			if s == 'v' {
				sy++
			}
			if s == '<' {
				sx--
			}
			if s == '>' {
				sx++
			}
			houses[Coord{sx, sy}]++

		} else {
			if s == '^' {
				ry--
			}
			if s == 'v' {
				ry++
			}
			if s == '<' {
				rx--
			}
			if s == '>' {
				rx++
			}
			houses[Coord{rx, ry}]++
		}

		// switch turn
		santasTurn = !santasTurn
	}

	count := 0
	for _, n := range houses {

		if n >= 1 {
			count++
		}
	}

	fmt.Println(count)
	return count
}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	str := string(bytes)

	part1(">")
	part1("^>v<")
	part1("^v^v^v^v^v")
	part1(str)

	part2("^v")
	part2("^>v<")
	part2("^v^v^v^v^v")
	part2(str)

}
