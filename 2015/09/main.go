package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	s "strings"
)

type Path struct {
	from, to string
}

var paths = map[Path]int{}
var minDistance = 99999
var maxDistance = 0

func contains(arr []string, s string) bool {
	for _, v := range arr {
		if v == s {
			return true
		}
	}
	return false
}

func computeMin(a []string) {
	dist := 0
	for i := 0; i < len(a)-1; i++ {
		if val, ok := paths[Path{a[i], a[i+1]}]; ok {
			dist += val
		} else {
			return
		}
	}

	//fmt.Println(a, dist)

	if dist < minDistance {
		minDistance = dist
	}

	if dist > maxDistance {
		maxDistance = dist
	}

}

func permute(arr []string, n int) {
	if n == 1 {
		computeMin(arr)
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
	lines := s.Split(string(bytes), "\n")

	cities := []string{}

	for _, line := range lines {
		if line == "" {
			continue
		}

		a := s.Split(line, " = ")
		b := s.Split(a[0], " to ")
		n, _ := strconv.Atoi(a[1])

		// from example, both ways possible
		paths[Path{b[0], b[1]}] = n
		paths[Path{b[1], b[0]}] = n

		if !contains(cities, b[0]) {
			cities = append(cities, b[0])
		}

		if !contains(cities, b[1]) {
			cities = append(cities, b[1])
		}

	}

	permute(cities, len(cities))

	fmt.Println(minDistance)
	fmt.Println(maxDistance)

}
