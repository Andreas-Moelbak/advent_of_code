package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"time"
)

func GetMD5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func main() {
    start := time.Now()
    baseString := "ckczppom"

    num := 1
    for {
        arg := baseString + strconv.Itoa(num)
        hash := GetMD5Hash(arg)
        if hash[:6] == "000000" {
            fmt.Println(hash)
            fmt.Println(num)
            break
        }
        num++
    }
    fmt.Println(time.Since(start))
}
