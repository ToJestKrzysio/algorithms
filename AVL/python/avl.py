from __future__ import annotations

from typing import Optional


class Tree:
    root: Node

    def __init__(self):
        self.root = Node()

    def __str__(self, *args, **kwargs):
        return self.root.__str__(*args, **kwargs)

    @classmethod
    def build(cls, array: list) -> Tree:
        tree = cls()
        for value in array:
            tree.root.insert(value)
        return tree


class Node:
    value: Optional[int]
    left: Optional[Node]
    right: Optional[Node]
    height: int

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.height = -1

    def insert(self, value: int) -> None:
        if self.value is None:
            self.value = value
            self.left = Node()
            self.right = Node()
        elif value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        self.update_height()

    def update_height(self) -> None:
        self.height = max(self.left.height, self.right.height) + 1

    def __bool__(self):
        return self.value is not None

    def __str__(self, spacer_width=0, recursive=False):
        if recursive is False:
            lines, empty = spacer_width // 2, spacer_width // 2 + spacer_width % 2
            if self.value:
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
    tree = Tree.build([5, 3, 7, 1, 8, 4, 9, 5, 6, 0, 8, 4, 3, 6, 2, 1, 8])
    print(tree.__str__(recursive=True))
