package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

/*

IMPLEMENTATION NOTES
====================

A lot of brute force here. Find all possible combinations of the numbers and see
if the sum is equal to total for each bucket. However, there are some
optimizations:

- find the length of smallest sets that have the target sum, and only consider
  the sets of that length for the first group
- while computing sets, once a combination is found, skip any other combinations
  that have the current first group, because the QE is all that matters

*/

var groups = [4][]int{}
var groupsCount = 0
var minQE = 0
var minLen = 0
var skip = false

// recurse groupsCount levels deep to find all possible combiations
func findSetWithSum(weights []int, total, group, setLength int) {

	// if we're groupsCount level deep, we've found a matching condition
	// ie, all groups contain packages having same total weight
	if group == groupsCount {

		// find QE value
		qe := 1
		for _, v := range groups[0] {
			qe *= v
		}

		// setting min for the first time
		if minQE == 0 || qe < minQE {
			minQE = qe
			minLen = len(groups[0])
		}

		// we found one set. skip the rest of combinations
		skip = true

		fmt.Println(groups, "QE:", qe)

		return
	}

	// find all possible combinations of weights
	for i := 1; i < 1<<uint(len(weights)); i++ {
		sum := 0
		groups[group] = []int{}
		remaining := []int{}

		for j := uint(0); j < uint(len(weights)); j++ {
			if ((1 << j) & i) > 0 {
				sum += weights[j]
				groups[group] = append(groups[group], weights[j])
			} else {
				remaining = append(remaining, weights[j])
			}
		}

		if sum == total {
			// we've found the combination which has the target sum

			if group == 0 { // first group

				// we can skip if the first group has a different length
				if len(groups[0]) != setLength {
					continue
				}

				// calculate QE and if it's larger, no need to proceed
				qe := 1
				for _, v := range groups[0] {
					qe *= v
				}

				if minQE != 0 && qe >= minQE {
					continue
				}
			}

			// find combination for the next group
			findSetWithSum(remaining, total, group+1, setLength)

			// after return, skip other combinations if not first group
			if group == 0 {
				skip = false
			}
			if skip {
				return
			}

		}
	}

}

func findSetsCount(weights []int, total int) int {

	min := 99999

	for i := 1; i < 1<<uint(len(weights)); i++ {
		sum := 0
		w := []int{}

		for j := uint(0); j < uint(len(weights)); j++ {
			if ((1 << j) & i) > 0 {
				sum += weights[j]
				w = append(w, weights[j])
			}
		}

		if sum == total {
			if len(w) < min {
				min = len(w)
			}
		}
	}

	return min
}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")

	weights := []int{}
	total := 0
	for _, line := range strings.Split(string(bytes), "\n") {
		if line == "" {
			continue
		}
		n, _ := strconv.Atoi(line)
		weights = append(weights, n)
		total += n
	}

	// part 1
	minQE, minLen, groupsCount = 0, 0, 3
	//minQE, minLen, groupsCount = 0, 0, findSetsCount(weights, total/3)
	findSetWithSum(weights, total/3, 0, 6)
	fmt.Println("Part 1:", minQE)

	// part 2
	minQE, minLen, groupsCount = 0, 0, 4
	//minQE, minLen, groupsCount = 0, 0, findSetsCount(weights, total/4)
	findSetWithSum(weights, total/4, 0, 5)
	fmt.Println("Part 2:", minQE)

}
