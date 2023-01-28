package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	data, err := os.ReadFile("./day1.input")
	check(err)

	sum := 0
	solved := false
	for i, d := range data {
		s := rune(d)
		if s == '(' {
			sum++
		} else {
			sum--
		}
		if sum == -1 && !solved {
			defer fmt.Println(i + 1)
			solved = true
		}
	}
	fmt.Println(sum)
}
