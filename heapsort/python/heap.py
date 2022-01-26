from __future__ import annotations

from typing import List


class Heap(list):

    def max_heapify(self, n: int) -> None:
        left_id = 2 * (n + 1) - 1
        right_id = 2 * (n + 1)
        max_id = n
        try:
            max_id = max_id if self[max_id] >= self[left_id] else left_id
        except IndexError:
            return
        try:
            max_id = max_id if self[max_id] >= self[right_id] else right_id
        except IndexError:
            pass
        if n != max_id:
            self[n], self[max_id] = self[max_id], self[n]
            self.max_heapify(max_id)

    @classmethod
    def build_max(cls, array: List) -> Heap:
        heap = Heap(array)
        for node_id in range(len(heap) // 2 - 1, -1, -1):
            heap.max_heapify(node_id)
        return heap


def heapsort(array: List) -> List:
    heap = Heap.build_max(array)
    sorted_list = [None] * len(heap)
    while heap:
        sorted_list[len(heap) - 1] = heap[0]
        heap[0] = heap[-1]
        del heap[-1]
        heap.max_heapify(0)
    return sorted_list


if __name__ == '__main__':
    array = [5, 3, 7, 6, 2, 1, 4]
    heap = Heap.build_max(array)
    print(heap)
    print(heapsort(array))
