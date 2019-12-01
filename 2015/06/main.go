package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

type Coord struct {
	x, y int
}

func parse(str string) (string, Coord, Coord) {
	reInstr := regexp.MustCompile(`[a-z ]+`)
	reCoord := regexp.MustCompile(`[0-9]+`)

	instr := strings.Trim(reInstr.FindString(str), " ")
	coord := reCoord.FindAllString(str, -1)

	var c []int

	for i := range coord {
		n, _ := strconv.Atoi(coord[i])
		c = append(c, n)
	}

	//fmt.Println(c)

	return instr, Coord{c[0], c[1]}, Coord{c[2], c[3]}
}

func part1(str string) {

	lines := strings.Split(str, "\n")

	lights := make(map[Coord]bool)

	for _, line := range lines {
		if line != "" {
			instr, from, to := parse(line)

			for x := from.x; x <= to.x; x++ {
				for y := from.y; y <= to.y; y++ {
					if instr == "turn on" {
						lights[Coord{x, y}] = true

					}
					if instr == "turn off" {
						lights[Coord{x, y}] = false
					}

					if instr == "toggle" {
						lights[Coord{x, y}] = !lights[Coord{x, y}]
					}

				}
			}

		}
	}

	count := 0
	for _, status := range lights {
		if status {
			count++
		}
	}

	fmt.Println(count)

}

func part2(str string) {

	lines := strings.Split(str, "\n")

	lights := make(map[Coord]int)

	for _, line := range lines {
		if line != "" {
			instr, from, to := parse(line)

			for x := from.x; x <= to.x; x++ {
				for y := from.y; y <= to.y; y++ {
					if instr == "turn on" {
						lights[Coord{x, y}]++

					}
					if instr == "turn off" {
						lights[Coord{x, y}]--
						if lights[Coord{x, y}] < 0 {
							lights[Coord{x, y}] = 0
						}
					}

					if instr == "toggle" {
						lights[Coord{x, y}] += 2
					}

				}
			}

		}
	}

	count := 0
	for _, value := range lights {
		count += value
	}

	fmt.Println(count)

}

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	str := string(bytes)

	//fmt.Println(parse("turn off 660,55 through 986,197"))
	//fmt.Println(parse("toggle 322,558 through 977,958"))
	//fmt.Println(parse("turn on 226,196 through 599,390"))

	//part1("turn on 0,0 through 999,999")
	part1(str)
	part2(str)

}
