package main

import (
	"fmt"
	"math"
)

// get factors of a  number as fast as possible
func getFactors(n int) []int {

	factors := []int{}

	step := 1
	if n%2 != 0 {
		step = 2
	}

	for i := 1; i < int(math.Sqrt(float64(n)))+1; i += step {

		if n%i == 0 {
			factors = append(factors, i)

			if i != n/i {
				factors = append(factors, n/i)
			}
		}
	}

	return factors

}

func part1(input int) {

	houseNumber := 1

	for {

		// the number of presents each house gets is its factors times 10
		sum := 0
		for _, f := range getFactors(houseNumber) {
			sum += f * 10
		}

		if sum >= input {
			fmt.Println("Part 1:", houseNumber)
			return
		}

		houseNumber++
	}
}

// same as part 1, but keep track of elves this time
// and multiply by 11 (instead of 10)
func part2(input int) {

	// keep track of elves visit count
	elvesVisit := make(map[int]int)

	houseNumber := 1

	for {

		// the number of presents each house gets is its factors times 11
		sum := 0
		for _, f := range getFactors(houseNumber) {
			if elvesVisit[f] < 50 {
				sum += f * 11
				elvesVisit[f]++
			}
		}

		if sum >= input {
			fmt.Println("Part 2:", houseNumber)
			return
		}

		houseNumber++

	}

}

func main() {

	input := 33100000

	part1(input)

	part2(input)

}
