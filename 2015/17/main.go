package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	containers := []int{}

	for _, line := range lines {
		if line == "" {
			continue
		}
		n, _ := strconv.Atoi(line)
		containers = append(containers, n)
	}

	count := 0
	minSetSize := len(containers)
	minSetCount := 0

	// compute all possible combinations
	// using bit method: https://en.wikipedia.org/wiki/Power_set#Representing_subsets_as_functions
	for i := 1; i < int(math.Pow(2, float64(len(containers)))); i++ {
		set := []int{}
		for j := 0; j < len(containers); j++ {
			if ((1 << uint(j)) & i) > 0 {
				set = append(set, containers[j])
			}
		}

		// sum the set
		sum := 0
		for _, n := range set {
			sum += n
		}

		//
		if sum == 150 {
			// part 1
			count++

			// part 2
			if len(set) < minSetSize {
				minSetSize = len(set)
				minSetCount = 1
			} else if len(set) == minSetSize {
				minSetCount++
			}

		}

	}

	fmt.Println("part 1:", count)
	fmt.Println("part 2:", minSetCount)

}
