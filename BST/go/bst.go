package main

import (
	"errors"
	"fmt"
	"strconv"
)

type Node struct {
	value int
	left  *Node
	right *Node
}

func (node *Node) Insert(value int) bool {
	if value < node.value {
		if node.left == nil {
			node.left = &Node{value: value}
			return true
		} else {
			return node.left.Insert(value)
		}
	}

	if node.right == nil {
		node.right = &Node{value: value}
		return true
	} else {
		return node.right.Insert(value)
	}
}

func BuildTree(array []int) (Node, error) {
	node := Node{value: array[0]}
	for i := 1; i < len(array); i++ {
		if ok := node.Insert(array[i]); !ok {
			message := fmt.Sprintf("Insertion failed for element %v.", array[i])
			return node, errors.New(message)
		}
	}
	return node, nil
}

func (node Node) Print() string {
	line := ""
	if node.left != nil {
		line += node.left.Print()
	}
	line += strconv.Itoa(node.value) + " "
	if node.right != nil {
		line += node.right.Print()
	}
	return line
}

func (node Node) Sort() (sortedArray []int) {
	if node.left != nil {
		sortedArray = append(sortedArray, node.left.Sort()...)
	}
	sortedArray = append(sortedArray, node.value)
	if node.right != nil {
		sortedArray = append(sortedArray, node.right.Sort()...)
	}
	return sortedArray
}

func main() {
	array := []int{5, 3, 7, 1, 8, 4, 9}
	tree, err := BuildTree(array)
	if err != nil {
		fmt.Print(err)
	}
	result1 := tree.Print()
	fmt.Printf("%v, %T\n", result1, result1)
	result2 := tree.Sort()
	fmt.Printf("%v, %T\n", result2, result2)
}
