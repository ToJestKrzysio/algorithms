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
	height int
	weight int
}

func NewNode(value int) *Node {
	return &Node{value: &value, height: 0, weight: 0}
}

func emptyNode() *Node {
	return &Node{value: nil, height: 0, weight: 0}
}

func (node *Node) Insert(value int) *Node {
	if value < *node.value {
		if node.left == nil {
			node.left = NewNode(value)
		} else {
			node.left = node.left.Insert(value)
		}
	} else {
		if node.right == nil {
			node.right = NewNode(value)
		} else {
			node.right = node.right.Insert(value)
		}
	}
	node.updateHeightAndWeight()
	return node.fixAVL()
}

func (node *Node) fixAVL() *Node {
	newNode := node
	for newNode.invalidAVL() {
		if newNode.weight > 0 {
			if newNode.right.weight < 0 {
				newNode.right = newNode.right.rightRotate()
			}
			newNode = newNode.leftRotate()
		} else {
			if newNode.left.weight > 0 {
				newNode.left = newNode.left.leftRotate()
			}
			newNode = newNode.rightRotate()
		}
		if newNode.left != nil {
			newNode.left = newNode.left.fixAVL()
		}
		if newNode.right != nil {
			newNode.right = newNode.right.fixAVL()
		}
	}
	newNode.updateHeightAndWeight()
	return newNode
}

func (node *Node) leftRotate() *Node {
	child, parent := node, node.right
	if parent.left != nil {
		parent = parent.rightRotate()
	}

	child.right = nil
	child.updateHeightAndWeight()

	parent.left = child
	parent.updateHeightAndWeight()

	return parent
}

func (node *Node) rightRotate() *Node {
	child, parent := node, node.left
	if parent.right != nil {
		parent = parent.leftRotate()
	}

	child.left = nil
	child.updateHeightAndWeight()

	parent.right = child
	parent.updateHeightAndWeight()

	return parent
}

func (node Node) invalidAVL() bool {
	return -1 > node.weight || node.weight > 1
}

func (node *Node) updateHeightAndWeight() {
	left := -1
	if node.left != nil {
		left = node.left.height
	}
	right := -1
	if node.right != nil {
		right = node.right.height
	}
	if left > right {
		node.height = left + 1
	} else {
		node.height = right + 1
	}
	node.weight = right - left
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
