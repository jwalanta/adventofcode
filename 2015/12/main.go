package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"strconv"
)

// part 1: just look for numbers and add them
func part1(s []byte) int {
	sum := 0
	num := ""

	for _, b := range s {
		if b == '-' || (b >= '0' && b <= '9') {
			num += string(b)
		} else {
			if num != "" {
				n, _ := strconv.Atoi(num)
				sum += n
				num = ""
			}
		}

	}
	return sum
}

// part 2: recursively parse json
func part2(data interface{}) int {

	sum := 0
	// data can be three things. array, object, or number

	switch d := data.(type) {

	// array
	case []interface{}:
		for _, v := range d {
			sum += part2(v)
		}

	// object
	case map[string]interface{}:

		// check if there are any reds
		red := false
		for _, v := range d {
			if v == "red" {
				red = true
				break
			}
		}

		if !red {
			for _, v := range d {
				sum += part2(v)
			}
		}

	// number
	case float64:
		sum += int(d)
	}

	return sum

}

func main() {

	bytes, _ := ioutil.ReadFile("input.txt")

	fmt.Println(part1(bytes))

	var input []interface{}
	err := json.Unmarshal(bytes, &input)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(part2(input))

}
