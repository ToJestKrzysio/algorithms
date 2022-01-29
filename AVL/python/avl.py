from __future__ import annotations

from typing import Optional


class Tree:
    root: Node

    def __init__(self):
        self.root = Node()

    def __str__(self):
        return self.root.__str__(recursive=True)

    @classmethod
    def build(cls, array: list) -> Tree:
        tree = cls()
        for value in array:
            tree.root = tree.root.insert(value)
        return tree


class Node:
    value: Optional[int]
    left: Optional[Node]
    right: Optional[Node]
    parent: Optional[Node]
    height: int
    weight: int

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.height = -1

    def insert(self, value: int) -> Node:
        if self.value == value:
            raise ValueError("This value already exists inside the tree.")
        self._insert(value)
        self.update_height()
        return self if self.avl else self.fix_avl()

    def fix_avl(self) -> Node:
        node = self
        while not node.avl:
            if node.weight > 0:
                if node.right.weight < 0:
                    node.right = node.right.right_rotate()
                node = node.left_rotate()
            else:
                if node.right.weight > 0:
                    node.left = node.left.left_rotate()
                node = node.right_rotate()
            node.left = node.left.fix_avl()
            node.right = node.right.fix_avl()
        return node

    def _insert(self, value: int) -> None:
        if not self:
            self.value = value
            self.left = Node()
            self.right = Node()
            return
        if value < self.value:
            self.left = self.left.insert(value)
            return
        self.right = self.right.insert(value)

    def update_height(self) -> None:
        self.height = max(self.left.height, self.right.height) + 1

    @property
    def weight(self) -> int:
        return self.right.height - self.left.height if self else 0

    @property
    def avl(self) -> bool:
        return self.weight in range(-1, 2)

    def left_rotate(self) -> Node:
        child = self
        parent = self.right
        if parent.left:
            parent = parent.right_rotate()

        child.right = Node()
        child.update_height()

        parent.left = child
        parent.update_height()

        return parent

    def right_rotate(self) -> Node:
        child = self
        parent = self.left
        if parent.right:
            parent = parent.left_rotate()

        child.left = Node()
        child.update_height()

        parent.right = child
        parent.update_height()

        return parent

    def __bool__(self):
        return self.value is not None

    def __str__(self, spacer_width=0, recursive=False):
        if recursive is False:
            lines, empty = spacer_width // 2, spacer_width // 2 + spacer_width % 2
            if self:
                left_spacer = " " * empty + "_" * lines
                right_spacer = "_" * lines + " " * empty
                value = str(self.value)
            else:
                left_spacer = right_spacer = " " * spacer_width
                value = " "
            return f"{left_spacer}{value}{right_spacer}"

        depth = 0
        max_height = self.height
        current_row = [self]
        lines = []
        while current_row:
            next_row = []
            finish = True
            line = ""
            spacer_width = int(2 ** (max_height - depth) - 1)
            for visited in current_row:
                line += visited.__str__(spacer_width=spacer_width) + " "
                next_row.append(visited.left if visited.left is not None else Node())
                next_row.append(visited.right if visited.right is not None else Node())
                if visited:
                    finish = False
            depth += 1
            lines.append(line)
            current_row = next_row
            if finish:
                break
        return "\n".join(lines[0:-1])


if __name__ == '__main__':
    tree = Tree.build([0, 1, 2, 3, 4, 5])
    print(tree)
