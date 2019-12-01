package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	s "strings"
)

func area(str string) int {

	p := s.Split(str, "x")
	l, _ := strconv.Atoi(p[0])
	w, _ := strconv.Atoi(p[1])
	h, _ := strconv.Atoi(p[2])

	a1 := l * w
	a2 := w * h
	a3 := h * l

	s := a1
	if a2 < s {
		s = a2
	}

	if a3 < s {
		s = a3
	}

	return 2*(a1+a2+a3) + s
}

func ribbon(str string) int {

	p := s.Split(str, "x")
	l, _ := strconv.Atoi(p[0])
	w, _ := strconv.Atoi(p[1])
	h, _ := strconv.Atoi(p[2])

	p1 := l + w
	p2 := w + h
	p3 := h + l

	s := p1
	if p2 < s {
		s = p2
	}

	if p3 < s {
		s = p3
	}

	return 2*(s) + (l * w * h)
}

func part1(str string) {
	lines := s.Split(str, "\n")
	totalArea := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		totalArea += area(line)
	}
	fmt.Println(totalArea)
}

func part2(str string) {
	lines := s.Split(str, "\n")
	totalLength := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		totalLength += ribbon(line)
	}
	fmt.Println(totalLength)
}

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	str := string(bytes)

	//fmt.Println(area("2x3x4"))
	//fmt.Println(ribbon("2x3x4"))
	//fmt.Println(ribbon("1x1x10"))

	part1(str)
	part2(str)
}
