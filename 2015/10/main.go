package main

import (
	"fmt"
	"strconv"
)

// DONT USE this. slower version using string
func looknsay(n string) string {
	last := string(n[0])
	str := ""
	count := 1

	for i := 1; i < len(n); i++ {
		if last != string(n[i]) {
			str += strconv.Itoa(count) + last
			count = 0
			last = string(n[i])
		}
		count++
	}

	str += strconv.Itoa(count) + last

	return str
}

// faster version with integer array
func looknsayv2(n []int) []int {
	last := n[0]
	a := []int{}
	count := 1

	for i := 1; i < len(n); i++ {
		if last != n[i] {
			a = append(a, count)
			a = append(a, last)
			count = 0
			last = n[i]
		}
		count++
	}
	a = append(a, count)
	a = append(a, last)

	return a

}

func main() {

	// s := "1321131112"
	// for i := 0; i < 40; i++ {
	// 	fmt.Println(i)
	// 	s = looknsay(s)
	// }

	// //fmt.Println(s)
	// fmt.Println(len(s))

	// using array instead of string
	n := []int{1, 3, 2, 1, 1, 3, 1, 1, 1, 2}
	for i := 1; i <= 50; i++ {
		n = looknsayv2(n)

		if i == 40 || i == 50 {
			fmt.Println(len(n))
		}
	}

}
