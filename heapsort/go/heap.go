package main

import "fmt"

func BuildMaxHeap(array []int) []int {
	for nodeID := len(array)/2 - 1; nodeID >= 0; nodeID-- {
		array = maxHeapify(array, nodeID)
	}
	return array
}

func maxHeapify(array []int, n int) (heapified []int) {
	leftID := 2*(n+1) - 1
	rightID := 2 * (n + 1)
	if leftID >= len(array) {
		return array
	}
	maxID := n
	if array[leftID] >= array[maxID] {
		maxID = leftID
	}

	if len(array) > rightID && array[rightID] >= array[maxID] {
		maxID = rightID
	}

	if maxID != n {
		array[n], array[maxID] = array[maxID], array[n]
		array = maxHeapify(array, maxID)
	}
	return array
}

func HeapSort(array []int) []int {
	heap := BuildMaxHeap(array)
	sorted := make([]int, len(heap))
	for nodeID := len(heap) - 1; nodeID >= 0; nodeID-- {
		sorted[nodeID] = heap[0]
		heap[0] = heap[nodeID]
		heap = heap[:len(heap)-1]
		heap = maxHeapify(heap, 0)
	}
	return sorted
}

func main() {
	fmt.Print(BuildMaxHeap([]int{5, 3, 7, 6, 2, 1, 4}), "\n")
	fmt.Print(HeapSort([]int{5, 3, 7, 6, 2, 1, 4}))
}
