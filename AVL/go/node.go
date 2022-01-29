package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

type Node struct {
	value  *int
	left   *Node
	right  *Node
	parent *Node
	height int
	weight int
}

func NewNode(value int, parent *Node) *Node {
	return &Node{value: &value, height: 0, weight: 0, parent: parent}
}

func emptyNode() *Node {
	return &Node{value: nil, height: 0, weight: 0}
}

func (node *Node) Insert(value int) *Node {
	if value < *node.value {
		if node.left == nil {
			node.left = NewNode(value, node)
		} else {
			node.left = node.left.Insert(value)
		}
	} else {
		if node.right == nil {
			node.right = NewNode(value, node)
		} else {
			node.right = node.right.Insert(value)
		}
	}
	node.height = node.updateHeight()
	return node
}

func (node Node) updateHeight() int {
	left := -1
	if node.left != nil {
		left = node.left.height
	}
	right := -1
	if node.right != nil {
		right = node.right.height
	}
	if left > right {
		return left + 1
	}
	return right + 1
}

func (node Node) Print() {
	toVisit := make([][]Node, node.height+1)
	toVisit[0] = append(toVisit[0], node)
	var lines []string
	for i := 0; i <= node.height; i++ {
		var line []string
		for _, visitedNode := range toVisit[i] {
			line = append(line, visitedNode.toString(node.height-i))
			if len(toVisit) > i+1 {
				if visitedNode.left != nil {
					toVisit[i+1] = append(toVisit[i+1], *visitedNode.left)
				} else {
					toVisit[i+1] = append(toVisit[i+1], *emptyNode())
				}
				if visitedNode.right != nil {
					toVisit[i+1] = append(toVisit[i+1], *visitedNode.right)
				} else {
					toVisit[i+1] = append(toVisit[i+1], *emptyNode())
				}
			}
		}
		lines = append(lines, strings.Join(line, " "))
	}
	fmt.Print(strings.Join(lines, "\n"))

}

func (node Node) toString(height int) string {
	spacerWidth := int(math.Pow(2, float64(height))) - 1
	var value, leftSpacer, rightSpacer string
	if node.value == nil {
		value = " "
		leftSpacer = strings.Repeat(" ", spacerWidth)
		rightSpacer = strings.Repeat(" ", spacerWidth)
	} else {
		value = strconv.Itoa(*node.value)
		lines := strings.Repeat("_", spacerWidth/2)
		blanks := strings.Repeat(" ", spacerWidth/2+spacerWidth%2)
		leftSpacer = blanks + lines
		rightSpacer = lines + blanks
	}
	return fmt.Sprintf("%s%v%s", leftSpacer, value, rightSpacer)
}

func main() {
	tree := NewTree([]int{0, 1, 2, 3, 4, 5})
	tree.Print()
}
