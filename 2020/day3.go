package main

import (
	"fmt"
	"os"
	"strings"
)

func generateForrest(dat []string, width int) []string {
	forrestHeight := len(dat)
	forrestWidth := (forrestHeight * width) + 1

	for idx := range dat {
		if dat[idx] != "" {
			for {
				dat[idx] += dat[idx]
				if len(dat[idx]) > forrestWidth {
					break
				}
			}
		}
	}
	return dat
}

func traverseForrest(forrest []string, step []int) int {
	metTrees := 0
	pos := step[1]
	for i := range forrest {
		if i > 0 && i%step[0] == 0 {
			if string(forrest[i][pos]) == "#" {
				metTrees++
			}
			pos += step[1]
		}
	}
	return metTrees
}

func stripSlice(s []string) []string {
	var newSlice []string
	for _, line := range s {
		if line != "" {
			newSlice = append(newSlice, line)
		}
	}
	return newSlice
}

func main() {
	dat, _ := os.ReadFile("day3.input")
	stringData := strings.Split(string(dat), "\n")
	runs := [][]int{{1, 1}, {1, 3}, {1, 5}, {1, 7}, {2, 1}}

	stringData = stripSlice(stringData)
	forrest := generateForrest(stringData, 7)
    sum := 1
    for _, run := range runs  {
	    result := traverseForrest(forrest, run)
        sum *= result
        fmt.Println(result, sum)
    }
}
