package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func min(a int, b int, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	} else {
		return c
	}
}

func least(a int, b int, c int) (least int, second int) {
	if a <= b && a <= c {
		least = a
		if c <= b {
			second = c
		} else {
			second = b
		}
	} else if b <= a && b <= c {
		least = b
		if a <= c {
			second = a
		} else {
			second = c
		}
	} else {
		least = c
		if b <= a {
			second = b
		} else {
			second = a
		}
	}
	return
}

func main() {
	dat, err := os.ReadFile("day2.input")
	check(err)

	sdat := strings.Split(string(dat), "\n")
	solve1sum := 0
	solve2sum := 0

	for _, v := range sdat {
		pack := strings.Split(v, "x")
		if v != "" {
			l, _ := strconv.Atoi(pack[0])
			w, _ := strconv.Atoi(pack[1])
			h, _ := strconv.Atoi(pack[2])
			//part1
			slack := min(l*w, w*h, h*l)
			area := 2*l*w + 2*w*h + 2*h*l
			solve1sum += slack + area

			//part2
			least, second := least(l, w, h)
			ribbon := least*2 + second*2
			bow := l * w * h
			solve2sum += ribbon + bow
		}
	}
	fmt.Println(solve1sum)
	fmt.Println(solve2sum)
}
