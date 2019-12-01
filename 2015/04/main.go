package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func getMD5Hash(text string) string {
	hasher := md5.New()
	hasher.Write([]byte(text))
	return hex.EncodeToString(hasher.Sum(nil))
}

func part12(str string, zeroes int) {
	n := 0
	text := ""
	md5 := ""
	for {

		text = str + strconv.Itoa(n)
		md5 = getMD5Hash(text)
		//fmt.Printf("%s %d\n", md5, n)
		if md5[0:zeroes] == strings.Repeat("0", zeroes) {
			fmt.Println(n)
			break
		}

		n++
	}

}

func main() {
	//part12("abcdef", "00000")
	part12("ckczppom", 5)
	part12("ckczppom", 6)
}
