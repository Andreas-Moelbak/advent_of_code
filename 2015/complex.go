package main

import "fmt"


func main() {
    start := 0 + 0i
    left := -1 + 0i
    right := 1 + 0i
    up := 0 + 1i
    down := 0 - 1i
    fmt.Println(left)
    fmt.Println(right)
    fmt.Println(up)
    fmt.Println(down)
    fmt.Println(start)
    fmt.Println(start + right)
    dict := make(map[complex128]int)
    dict[start] = 0
    fmt.Println(dict)
    dict[start] = dict[start] + 1
    fmt.Println(dict)
}
