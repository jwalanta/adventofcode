package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type properties struct {
	capacity, durability, flavor, texture, calories int
}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	var ingredient = []properties{}

	for _, line := range lines {

		if line == "" {
			continue
		}

		p := strings.Split(line, " ")

		c, _ := strconv.Atoi(strings.Trim(p[2], ","))
		d, _ := strconv.Atoi(strings.Trim(p[4], ","))
		f, _ := strconv.Atoi(strings.Trim(p[6], ","))
		t, _ := strconv.Atoi(strings.Trim(p[8], ","))
		cal, _ := strconv.Atoi(strings.Trim(p[10], ","))
		ingredient = append(ingredient, properties{c, d, f, t, cal})
	}

	maxScore := 0
	maxLowCalScore := 0

	for a := 0; a <= 100; a++ {
		for b := 0; b <= 100-a; b++ {
			for c := 0; c <= 100-a-b; c++ {
				d := 100 - a - b - c

				quantity := []int{a, b, c, d}
				capacity, durability, flavor, texture, calories := 0, 0, 0, 0, 0

				for i := 0; i < 4; i++ {
					capacity += quantity[i] * ingredient[i].capacity
					durability += quantity[i] * ingredient[i].durability
					flavor += quantity[i] * ingredient[i].flavor
					texture += quantity[i] * ingredient[i].texture
					calories += quantity[i] * ingredient[i].calories
				}

				if capacity < 0 {
					capacity = 0
				}

				if durability < 0 {
					durability = 0
				}

				if flavor < 0 {
					flavor = 0
				}

				if texture < 0 {
					texture = 0
				}

				score := capacity * durability * flavor * texture

				if score > maxScore {
					maxScore = score
				}

				if calories == 500 && score > maxLowCalScore {
					maxLowCalScore = score
				}
			}
		}
	}

	fmt.Println("part 1:", maxScore)
	fmt.Println("part 2:", maxLowCalScore)

}
