package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"sort"
	"strings"
)

type replacement struct {
	from, to string
}

var replacements []replacement
var med string

// get array of all possible replacements
func getReplacements(str, from, to string) []string {

	//fmt.Println(med, from, to)

	replaced := make(map[string]bool)

	for i := 0; i < len(str); i++ {
		s := strings.Replace(str[i:], from, to, 1)
		if s != str[i:] {
			replaced[str[:i]+s] = true
		}
	}

	rep := []string{}
	for k := range replaced {
		rep = append(rep, k)
	}

	return rep

}

// DO NOT USE
// this will probably never finish computing or will take a long time
// try every replacements to generate reduced formulas to get to "e"
func reduceTillE(s string, n int) {
	//fmt.Println(n, s)

	if s == "e" {
		fmt.Println("Part 2:", n)
		os.Exit(0)
		return
	}

	for _, r := range replacements {
		if strings.Count(s, r.to) == 0 {
			continue
		}
		lst := getReplacements(s, r.to, r.from)
		for _, replaced := range lst {
			reduceTillE(replaced, n+1)
		}
	}

}

// part 2: got the idea from reddit thread
// instead of trying to find every possible reduction, randomly use a pair and
// hope it works. surprisingly it works!
func reduceRandomly(s string) int {

	step := 1

	// sometimes the reduction goes in rabbit hole
	// lets not go 1000 levels deeper
	for i := 1; i < 1000; i++ {
		r := replacements[rand.Intn(len(replacements))]
		if strings.Count(s, r.to) > 0 {
			lst := getReplacements(s, r.to, r.from)
			s = lst[rand.Intn(len(lst))]

			if s == "e" {
				return step
			}
			step++
		}
	}

	return 0

}

func part1() {
	replaced := make(map[string]bool)

	for _, sub := range replacements {
		for i := 0; i < len(med); i++ {
			str := strings.Replace(med[i:], sub.from, sub.to, 1)
			if str != med[i:] {
				replaced[med[:i]+str] = true
			}
		}
	}

	fmt.Println("part 1:", len(replaced))

}

// DO NOT USE. This wont work. Use part2Random() instead
func part2() {

	// sort the replacements by decending length of "to" to make the
	// replacement greedy

	sort.SliceStable(replacements, func(i, j int) bool {
		return len(replacements[i].to) > len(replacements[j].to)
	})

	// try to reduce recursively
	reduceTillE(med, 0)

}

func part2Random() {

	// lets hope we find the answer in at least 100 random trials
	for i := 0; i < 100; i++ {
		n := reduceRandomly(med)
		if n > 0 {
			fmt.Println("Part 2:", n)
			return
		}
	}

}

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	for _, line := range lines {
		if line == "" {
			continue
		}

		if strings.Contains(line, "=>") {
			p := strings.Split(line, " => ")
			replacements = append(replacements, replacement{p[0], p[1]})
		} else {
			med = line
		}

	}

	part1()

	part2Random()

}
