package main

func main() {

	// input
	row := 3010
	col := 3019

	// init values
	r, c, n := 1, 1, 20151125

	for {
		// find next
		r--
		c++

		if r == 0 {
			r = c
			c = 1
		}

		n = (n * 252533) % 33554393

		//fmt.Println(r, c, n)

		if r == row && c == col {
			break
		}

	}

}
