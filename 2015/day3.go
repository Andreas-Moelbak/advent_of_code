package main

import (
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	dat, err := os.ReadFile("day3.input")
	check(err)
	sdat := strings.Split(string(dat), "")

	moves := map[string]complex128{
		">": 1 + 0i,
		"<": -1 + 0i,
		"^": 0 + 1i,
		"v": 0 - 1i,
	}

	places := make(map[complex128]int)

	position := 0 + 0i
	for _, dir := range sdat {
		places[position] += 1
		position += moves[dir]
	}
    fmt.Println("Part 1:", len(places))

	santaPlaces := make(map[complex128]int)
    santaPos := 0 + 0i
    roboSantaPos := 0 + 0i
	for i, dir := range sdat {
        if i % 2 == 0 {
            santaPlaces[santaPos] += 1
            santaPos += moves[dir]
        } else {
            santaPlaces[roboSantaPos] += 1
            roboSantaPos += moves[dir]
        }
	}

    fmt.Println("Part 2:", len(santaPlaces))
}
