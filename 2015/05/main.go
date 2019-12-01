package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func countVowels(s string) int {
	return strings.Count(s, "a") + strings.Count(s, "e") + strings.Count(s, "i") + strings.Count(s, "o") + strings.Count(s, "u")
}

func twice(s string) bool {
	for i := range s {
		//fmt.Printf("%d %c\n", i, s[i])
		if i > 0 {
			if s[i-1] == s[i] {
				return true
			}
		}
	}
	return false
}

func magicStr(s string) bool {
	return strings.Contains(s, "ab") || strings.Contains(s, "cd") || strings.Contains(s, "pq") || strings.Contains(s, "xy")
}

func isNice(s string) bool {
	return countVowels(s) >= 3 && twice(s) && !magicStr(s)
}

func pair(s string) bool {
	for i := range s {
		if i > 0 {
			p := s[i-1 : i+1]
			n := strings.Count(s[i+1:], p)

			//fmt.Printf("%s %d", p, n)

			if n > 0 {
				return true
			}
		}
	}
	return false
}

func magicStr2(s string) bool {
	for i := range s {
		if i > 1 {
			if s[i-2] == s[i] {
				return true
			}
		}
	}
	return false
}

func isNice2(s string) bool {
	return pair(s) && magicStr2(s)
}

func part1(str string) int {
	lines := strings.Split(str, "\n")

	count := 0
	for _, line := range lines {
		if isNice(line) {
			count++
		}
	}

	return count

}

func part2(str string) int {
	lines := strings.Split(str, "\n")

	count := 0
	for _, line := range lines {
		if isNice2(line) {
			count++
		}
	}

	return count
}

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	str := string(bytes)

	//fmt.Println(countVowels("ugknbfddgicrmopn"))
	//fmt.Println(twice("ugknbfddgicrmopn"))
	//fmt.Println(magicStr("ugknbfddgicrmopn"))

	// fmt.Println(isNice("ugknbfddgicrmopn"))
	// fmt.Println(isNice("aaa"))
	// fmt.Println(isNice("jchzalrnumimnmhp"))
	// fmt.Println(isNice("haegwjzuvuyypxyu"))
	// fmt.Println(isNice("dvszwmarrgswjxmb"))
	fmt.Println(part1(str))

	// fmt.Println(pair("qjhvhtzxzqqjkmpb"))
	// fmt.Println(magicStr2("qjhvhtzxzqqjkmpb"))

	// fmt.Println()
	// fmt.Println(isNice2("qjhvhtzxzqqjkmpb"))
	// fmt.Println(isNice2("xxyxx"))
	// fmt.Println(isNice2("uurcxstgmygtbstg"))
	// fmt.Println(isNice2("ieodomkazucvgmuy"))

	fmt.Println(part2(str))

}
