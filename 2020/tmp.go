package main

import (
    "fmt"
)

func main() {
    slice := [][]int{{1,2},{2,1},{7,1}}

    for _, i := range slice {
        for _, j := range i {
            fmt.Println(j)
        }
    }
}
