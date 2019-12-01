package main

import "fmt"

/*
Passwords must include one increasing straight of at least three letters,
like abc, bcd, cde, and so on, up to xyz.
They cannot skip letters; abd doesn't count.
*/
func conditiona(b []byte) bool {
	for i := 2; i < len(b); i++ {
		if b[i-2] == b[i]-2 && b[i-1] == b[i]-1 {
			return true
		}
	}
	return false
}

/*
Passwords may not contain the letters i, o, or l, as these letters can be
mistaken for other characters and are therefore confusing.
*/
func conditionb(b []byte) bool {
	for _, v := range b {
		if v == 'i' || v == 'o' || v == 'l' {
			return false
		}
	}
	return true
}

/*
Passwords must contain at least two different, non-overlapping pairs of letters,
like aa, bb, or zz.
*/
func conditionc(b []byte) bool {
	pairs := make(map[string]int)
	for i := 1; i < len(b); i++ {
		if b[i-1] == b[i] {
			pairs[string([]byte{b[i-1], b[i]})]++
			i++ // shouldn't be overlapping
		}
	}
	if len(pairs) >= 2 {
		return true
	}

	return false

}

// increment byte at pos, handle carryover
func incr(b []byte, pos int) []byte {
	if pos < 0 {
		return append([]byte{'a'}, b...)
	}
	if b[pos] < 'z' {
		b[pos]++
		return b
	} else {
		// wraparound and carryover
		b[pos] = 'a'
		return incr(b, pos-1)
	}
}

func main() {
	str := []byte("hepxcrrq")
	//str := []byte("abcdefgh")

	count := 0
	for {

		str = incr(str, len(str)-1)

		if conditiona(str) && conditionb(str) && conditionc(str) {
			count++
			fmt.Printf("part %d: %s\n", count, str)
		}
		if count == 2 {
			break
		}
	}

}
