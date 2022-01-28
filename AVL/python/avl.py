from __future__ import annotations

from typing import Optional


class Node:
    value: Optional[Node]
    left: Optional[Node]
    right: Optional[Node]
    parent: Optional[Node]
    height: int  # negative left heavy, positive right heavy

    def __init__(self):
        self.height = -1
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.heavy = 0

    def insert(self, value):
        is_valid = self._insert(value)
        self.update_height()
        while not self.check_avl_property():
            if self.heavy > 1:
                if self.heavy * self.right.heavy < 0:
                    self.right.right_rotate()
                self.right.left_rotate()
            else:
                if self.heavy * self.right.heavy > 0:
                    self.left.left_rotate()
                self.left.right_rotate()
        return is_valid

    def _insert(self, value) -> bool:
        if self.value is None:
            self.value = value
            self.left = Node()
            self.left.parent = self
            self.right = Node()
            self.right.parent = self
            return True
        if value < self.value:
            self.left.insert(value)
            return True
        self.right.insert(value)
        return True

    def right_rotate(self):
        current_parent = self.parent
        current_node = self
        new_node = self.left

        current_parent.update_child(current_node, new_node)

        current_node.left = Node()
        current_node.parent = new_node
        current_node.update_height()

        new_node.right = current_node
        new_node.parent = current_parent
        new_node.update_height()
        return new_node

    def left_rotate(self):
        current_parent = self.parent
        current_node = self
        new_node = self.right

        current_parent.update_child(current_node, new_node)

        current_node.right = Node()
        current_node.update_height()
        current_node.parent = new_node

        new_node.left = current_node
        new_node.parent = current_parent
        new_node.update_height()

    def update_child(self, current_child, new_child):
        if self.left is current_child:
            self.left = new_child
        self.right = new_child

    def update_height(self):
        self.height = max(self.left.height, self.right.height) + 1
        self.heavy = self.right.height - self.left.height

    def check_avl_property(self) -> bool:
        return self.heavy in range(-1, 2)

    def __str__(self):
        lines, line = [], []
        to_visit = [self]
        current_height = self.height
        while to_visit:
            visited = to_visit.pop(0)
            if visited.left is not None:
                to_visit.append(visited.left)
            if visited.right is not None:
                to_visit.append(visited.right)
            spacer = " " * int(2 ** visited.height - 1)
            if current_height != visited.height:
                lines.append(" ".join(line))
                line = []
                current_height = visited.height
            value = " " if visited.value is None else visited.value
            line.append(f"{spacer}{value}{spacer}")
        return "\n".join(lines)

    @classmethod
    def build(cls, array: list) -> Node:
        node = Node()
        for value in array:
            node.insert(value)
        return node


if __name__ == '__main__':
    tree = Node.build([5, 3, 1])
    print(tree.left.left.value)
