package main

type Tree struct {
	root *Node
}

func NewTree(array []int) (tree Tree) {
	tree = Tree{root: NewNode(array[0])}
	for i := 1; i < len(array); i++ {
		tree.root = tree.root.Insert(array[i])
	}
	return tree
}

func (tree Tree) Print() {
	tree.root.Print()
}
