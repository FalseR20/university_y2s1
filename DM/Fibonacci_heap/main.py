from __future__ import annotations

import copy
from typing import Optional


class Node:
    def __init__(
            self, value: int,
            parent: Optional[Node] = None, child: Optional[Node] = None,
            left: Optional[Node] = None, right: Optional[Node] = None,
            is_del: bool = False
    ):
        self.value = value
        self.parent = parent
        self.child = child
        self.left = left
        self.right = right
        self.is_del = is_del

    def check(self) -> str:
        return f"{self.left.check() if self.left else ''}-" \
               f"{self.value} ({self.child.check() if self.child else ''})-" \
               f"{self.right.check() if self.right else ''}"


class FibHeap:
    def __init__(self, *args: int):
        self.__min: Optional[Node] = None
        self.__is_empty = True
        self.add(*args)

    def add(self, *args: int) -> None:
        for arg in args:
            if not self.__is_empty:
                node = Node(arg, left=self.__min, right=self.__min.right)
                if node.right:
                    node.right.left = node
                self.__min.right = node
                if node.value < self.__min.value:
                    self.__min = node
            else:
                self.__min = Node(arg)
                self.__is_empty = False

    def check(self) -> None:
        cursor = self.__min
        while cursor.left:
            cursor = cursor.left
        while cursor:
            if cursor == self.__min:
                print("min->", end='')
            print(cursor.value, cursor.child.check() if cursor.child else '', end='')
            cursor = cursor.right
        print()

    def get_min(self) -> int:
        return self.__min.value

    def __iadd__(self, other: FibHeap):
        other = copy.deepcopy(other)
        if self.__is_empty:
            return other
        if other.__is_empty:
            return self

        ref1 = self.__min
        ref2 = other.__min
        while ref1.right:
            ref1 = ref1.right
        while ref2.left:
            ref2 = ref2.left

        ref1.right, ref2.left = ref2, ref1
        if self.__min.value > other.__min.value:
            self.__min = other.__min
        return self

    def __add__(self, other):
        return copy.deepcopy(self).__iadd__(other)


def main():
    heap1 = FibHeap(5, 1, 3, 2, 4, 0)
    heap2 = FibHeap(7, 6)
    heap3 = heap1 + heap2
    heap3 += heap2
    heap1.check()
    heap2.check()
    heap3.check()


if __name__ == '__main__':
    main()
