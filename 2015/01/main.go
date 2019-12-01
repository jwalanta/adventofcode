package main

import "fmt"
import "io/ioutil"
import s "strings"

func part1(str string) {
	fmt.Println(s.Count(str, "(") - s.Count(str, ")"))
}

func part2(str string) {
	floor := 0
	for pos, char := range str {
		if char == ')' {
			floor--
		}

		if char == '(' {
			floor++
		}

		if floor < 0 {
			fmt.Println(pos + 1)
			break
		}

	}
}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")
	str := string(bytes)

	part1(str)
	part2(str)

}
