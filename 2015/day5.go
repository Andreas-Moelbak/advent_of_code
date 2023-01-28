package main

import (
	"fmt"
	"os"
	"strings"
)

func readData() []string {
	dat, _ := os.ReadFile("day5.input")
	return strings.Split(string(dat), "\n")
}

func matchRulesPart1(s string) bool {
	vowel := 0
	duplicate := false
	contains := false
	for i, char := range s {
        switch {
		case char == 'a':
			vowel++
		case char == 'e':
			vowel++
		case char == 'i':
			vowel++
		case char == 'o':
			vowel++
		case char == 'u':
			vowel++
        }

		if i > 0 && s[i] == s[i-1] {
			duplicate = true
		}
	}
	badStrings := []string{"ab", "cd", "pq", "xy"}
	for _, badString := range badStrings {
		if strings.Contains(s, badString) {
			contains = true
		}
	}
	if vowel > 2 && duplicate && !contains {
		return true
	} else {
		return false
	}
}

func main() {
	data := readData()

    sumPart1 := 0
    for _, line := range data {
        if matchRulesPart1(line) {
            sumPart1++
        }
	}
    fmt.Println(sumPart1)
}
