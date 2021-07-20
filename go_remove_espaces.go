package main

import (
	"fmt"
	"strings"
)

func stdSpaces(s string) string {
	return strings.Join(strings.Fields(s), " ")
}

func main() {
	text := " On  my   home world "
	std := "On my home world"

	text = stdSpaces(text)

	fmt.Println(text)
	fmt.Println(std)
	fmt.Println(text == std)
}
