package main

import (
    "fmt"
    "regexp"
    "strings"
)


func main() {
    text := " On  my   home world "
    std := "On my home world"

    space := regexp.MustCompile(`\s+`)
    text = strings.TrimSpace(space.ReplaceAllString(text, " "))

    fmt.Println(text)
    fmt.Println(std)
    fmt.Println(text == std)
}