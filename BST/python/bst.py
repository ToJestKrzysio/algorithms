from __future__ import annotations

from typing import Optional


class Node:
    value: Optional[int]
    left: Optional[Node]
    right: Optional[Node]

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, value: int) -> bool:
        """ Insert value into a binary tree. True if succeeded, False otherwise. """
        if self.value is None:
            self.value = value
            self.left = Node()
            self.right = Node()
            return True
        if value < self.value:
            return self.left.insert(value)
        return self.right.insert(value)

    def search_for(self, value: int) -> bool:
        """ Search for value inside a binary tree, True if found False otherwise. """
        if self.value is None:
            return False
        if value == self.value:
            return True
        if value < self.value:
            return self.left.search_for(value)
        if value > self.value:
            return self.right.search_for(value)

    @classmethod
    def build_tree(cls, array: list) -> Node:
        node = Node()
        for value in array:
            if node.insert(value) is False:
                raise ValueError(f"Insertion of element {value} failed.")
        return node

    def sort(self) -> list:
        if not self:
            return []
        sorted_values = []
        if self.left:
            sorted_values.extend(self.left.sort())
        sorted_values.append(self.value)
        if self.right:
            sorted_values.extend(self.right.sort())
        return sorted_values

    def __bool__(self):
        return bool(self.value)

    def __str__(self):
        if not self:
            return ""
        lines = []
        if self.left:
            lines.append(str(self.left))
        lines.append(str(self.value))
        if self.right:
            lines.append(str(self.right))
        return " ".join(lines)


if __name__ == '__main__':
    tree = Node.build_tree([5, 3, 7, 1, 8, 4, 9])
    print(tree.sort())
