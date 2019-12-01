package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	s "strings"
)

// [to] = instruction
var cmds = map[string]string{}

// store the computed signals. it'll take a long time to
// compute if the signals are not stored.
var values = map[string]uint16{}

func compute(w string) uint16 {

	// if signal is already computed, return it
	if val, ok := values[w]; ok {
		return val
	}

	// if it's a number, return
	if s.ContainsAny(w, "0123456789") {
		n, _ := strconv.ParseUint(w, 10, 16)
		return uint16(n)
	}

	cmd := cmds[w]
	p := s.Split(cmd, " ")

	//fmt.Println("computing ", w, " = ", cmd)
	//fmt.Scanln()

	if s.Contains(cmd, "AND") {
		values[w] = compute(p[0]) & compute(p[2])
	} else if s.Contains(cmd, "OR") {
		values[w] = compute(p[0]) | compute(p[2])
	} else if s.Contains(cmd, "LSHIFT") {
		values[w] = compute(p[0]) << compute(p[2])
	} else if s.Contains(cmd, "RSHIFT") {
		values[w] = compute(p[0]) >> compute(p[2])
	} else if s.Contains(cmd, "NOT") {
		values[w] = ^compute(p[1])
	} else {
		values[w] = compute(cmd)
	}
	return values[w]

}

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	lines := s.Split(string(bytes), "\n")

	for _, line := range lines {
		if line == "" {
			continue
		}
		p := s.Split(line, " -> ")
		cmds[p[1]] = p[0]
	}

	fmt.Println(compute("a"))

	// Now, take the signal you got on wire a, override wire b to that signal,
	// and reset the other wires (including wire a). What new signal is
	// ultimately provided to wire a?

	values["b"] = values["a"]
	for k := range values {
		if k != "b" {
			delete(values, k)
		}
	}

	fmt.Println(compute("a"))
}
