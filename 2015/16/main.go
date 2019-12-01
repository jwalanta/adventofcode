package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	ticker := make(map[string]int)
	ticker["children"] = 3
	ticker["cats"] = 7
	ticker["samoyeds"] = 2
	ticker["pomeranians"] = 3
	ticker["akitas"] = 0
	ticker["vizslas"] = 0
	ticker["goldfish"] = 5
	ticker["trees"] = 3
	ticker["cars"] = 2
	ticker["perfumes"] = 1

	// part 1
	for _, line := range lines {
		p := strings.Split(line, " ")

		matchCount := 0
		for i := 2; i < len(p); i += 2 {
			detect := strings.Trim(p[i], ":")
			value, _ := strconv.Atoi(strings.Trim(p[i+1], ","))
			if v, ok := ticker[detect]; ok {
				if v == value {
					matchCount++
				}
			}
		}

		if matchCount == 3 {
			fmt.Println("part 1:", strings.Trim(p[1], ":"))
		}

	}

	// part 2
	for _, line := range lines {
		p := strings.Split(line, " ")

		matchCount := 0
		for i := 2; i < len(p); i += 2 {
			detect := strings.Trim(p[i], ":")
			detectedValue, _ := strconv.Atoi(strings.Trim(p[i+1], ","))
			if rememberedValue, ok := ticker[detect]; ok {

				if detect == "cats" || detect == "trees" {
					if rememberedValue < detectedValue {
						matchCount++
					}
				} else if detect == "pomeranians" || detect == "goldfish" {
					if rememberedValue > detectedValue {
						matchCount++
					}
				} else {
					if rememberedValue == detectedValue {
						matchCount++
					}
				}

			}
		}

		if matchCount == 3 {
			fmt.Println("part 2:", strings.Trim(p[1], ":"))
		}

	}

}
