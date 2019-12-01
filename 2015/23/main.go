package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var instr = []string{}

func execute(a uint) uint {

	r := map[string]uint{"a": a, "b": 0}

	p := 0

	for {

		parts := strings.Split(instr[p], " ")

		switch parts[0] {
		case "hlf":
			r[parts[1]] /= 2
			p++
		case "tpl":
			r[parts[1]] *= 3
			p++
		case "inc":
			r[parts[1]]++
			p++
		case "jmp":
			j, _ := strconv.Atoi(parts[1])
			p += j
		case "jie":
			rr := strings.Trim(parts[1], ",")
			j, _ := strconv.Atoi(parts[2])
			if r[rr]%2 == 0 {
				p += j
			} else {
				p++
			}
		case "jio":
			rr := strings.Trim(parts[1], ",")
			j, _ := strconv.Atoi(parts[2])
			if r[rr] == 1 {
				p += j
			} else {
				p++
			}
		}

		if p >= len(instr) || instr[p] == "" {
			break
		}
	}

	return r["b"]

}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	instr = strings.Split(string(bytes), "\n")

	fmt.Println("Part 1:", execute(0))
	fmt.Println("Part 2:", execute(1))
}
