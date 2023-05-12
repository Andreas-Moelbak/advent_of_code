package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseOnePort(p string) int  {
	fields := []string{}

	for _, field := range strings.Split(p, " ") {
		fmt.Println(field)
		if field != "" {
			if field[:3] != "cid" {
				fields = append(fields, field)
                parsed := parseTwoPort(field)
			}
		}
	}
	return len(fields)
}

func parseTwoPort(p string) bool {
    field := p[:3]
    value := p[4:]


    switch field {
    case "byr":
        value, _ = strconv.Atoi(value)
        if value > 1920 && value < 2002 {
            return true
        }
    case "iyr":
    case "eyr":
    case "hgt":
    case "hcl":
    case "ecl":
    case "pid":
    }
}

func main() {
	data, _ := os.ReadFile("./day4.input")
	stringData := strings.Split(string(data), "\n\n")
	result := 0
	for _, passport := range stringData {
		passport := strings.ReplaceAll(passport, "\n", " ")
		fields := parseOnePort(passport)
		if fields == 7 {
			result++
		}
        break
	}
	fmt.Println(result)
}
