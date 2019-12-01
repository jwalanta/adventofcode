package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type person struct {
	a, b string
}

var happiness = map[person]int{}
var maxHappiness = 0

func appendIfUnique(arr []string, s string) []string {
	for _, v := range arr {
		if v == s {
			return arr
		}
	}
	return append(arr, s)
}

func computeHappiness(p []string) int {

	//fmt.Println(p)

	sum := 0

	for i := 0; i < len(p); i++ {
		prev := i - 1
		if prev < 0 {
			prev = len(p) - 1
		}

		next := (i + 1) % len(p)

		// fmt.Println(p[i], p[prev], happiness[person{p[i], p[prev]}])
		// fmt.Println(p[i], p[next], happiness[person{p[i], p[next]}])

		sum += happiness[person{p[i], p[prev]}] + happiness[person{p[i], p[next]}]

	}

	return sum
}

// just circular permutation should be enough, but brute forcing using regular
// permutation because the list is small
func permute(arr []string, n int) {
	if n == 1 {
		h := computeHappiness(arr)

		if h > maxHappiness {
			maxHappiness = h
		}
	} else {
		for i := 0; i < n; i++ {

			permute(arr, n-1)
			if n%2 == 0 {
				arr[0], arr[n-1] = arr[n-1], arr[0]
			} else {
				arr[i], arr[n-1] = arr[n-1], arr[i]
			}
		}
	}
}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	persons := []string{}

	for _, line := range lines {
		if line == "" {
			continue
		}
		p := strings.Split(line, " ")
		n, _ := strconv.Atoi(p[3])

		if p[2] == "lose" {
			n = -n
		}

		p[10] = strings.Trim(p[10], ".")
		happiness[person{p[0], p[10]}] = n

		persons = appendIfUnique(persons, p[0])
		persons = appendIfUnique(persons, p[10])
	}

	// for p, v := range happiness {
	// 	fmt.Println(p.a, p.b, v)
	// }

	// for _, v := range persons {
	// 	fmt.Println(v)
	// }

	// part 1
	permute(persons, len(persons))
	fmt.Println("part 1:", maxHappiness)

	// part 2
	// add myself to group
	persons = append(persons, "Me")
	for _, v := range persons {
		happiness[person{"Me", v}] = 0
		happiness[person{v, "Me"}] = 0
	}

	maxHappiness = 0
	permute(persons, len(persons))
	fmt.Println("part 2:", maxHappiness)

}
