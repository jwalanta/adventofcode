package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	s "strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	lines := s.Split(string(bytes), "\n")

	rawCount := 0
	unquotedCount := 0
	quotedCount := 0

	for _, line := range lines {
		if line == "" {
			continue
		}

		rawCount += len(line)

		parsed, _ := strconv.Unquote(line)
		unquotedCount += len(parsed)

		quotedCount += len(strconv.Quote(line))
	}

	fmt.Println(rawCount - unquotedCount)
	fmt.Println(quotedCount - rawCount)

}
