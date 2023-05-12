package main

import (
	"os"
    "strings"
)

func loadInput() []string {
    data, _ := os.ReadFile("./day6.input")
    return strings.Split(string(data), "\n")
}

func main() {
    data := loadInput()
    //grid := [1000][1000]bool{}
    for _, i := range data {
        i := strings.Split(i, " ")
        if i[0] == "toggle" {
            //toggle()
        }
        switch i[1] {
        case "on": println("on")
        case "off": println("off")
        }
    }
}
