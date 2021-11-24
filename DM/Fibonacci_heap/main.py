# http://cppalgo.blogspot.com/2011/11/fibonacci-heap.html

from __future__ import annotations
import copy
from typing import Optional


class Node:
    def __init__(
            self, value: int, child: Optional[Node] = None,
            left: Optional[Node] = None, right: Optional[Node] = None
    ):
        self.value = value
        self.child = child
        self.left = left
        self.right = right
        self.depth: int = 1

    def check(self) -> str:
        to_print = str(self.value)
        if self.child:
            to_print += "(" + self.child.check() + ")"
        to_print += " "
        if self.right:
            to_print += self.right.check()
            return to_print
        return to_print[:-1]


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
        if self.__is_empty:
            print("empty")
        else:
            cursor = self.__min
            to_print = ""
            while cursor.left:
                cursor = cursor.left
            while cursor:
                if cursor.value == self.__min.value:
                    to_print += "`"
                to_print += str(cursor.value)
                if cursor.child:
                    to_print += "(" + cursor.child.check() + ")"
                to_print += "-"
                cursor = cursor.right
            print(to_print[:-1])

    def get_min(self) -> int:
        return self.__min.value

    def pop(self):
        pop_value, tail = self.__min.value, self.__min.child
        cursor: Optional[Node] = None
        if self.__min.left:
            self.__min.left.right = self.__min.right
            cursor = self.__min.left
            while cursor.left:
                cursor = cursor.left
        if self.__min.right:
            self.__min.right.left = self.__min.left
            if not cursor:
                cursor = self.__min.right
        del self.__min
        self.__min = cursor  # __min is not actual
        if tail:
            if self.__min:
                tail_heap = FibHeap()
                tail_heap.__min = tail
                tail_heap.__is_empty = False
                self.__iadd__(tail_heap)  # __min is not actual
            else:
                self.__is_empty = False
                self.__min = tail
                cursor = tail
                while cursor.left:
                    cursor = cursor.left
        elif not self.__min:
            self.__is_empty = True
            return pop_value

        # Consolidate stage
        while cursor:
            while cursor.left and cursor.depth == cursor.left.depth:
                if cursor.left.value > cursor.value:
                    max_node = cursor.left
                    cursor.left = cursor.left.left
                    if cursor.left:
                        cursor.left.right = cursor
                else:
                    cursor, max_node = cursor.left, cursor
                    cursor.right = max_node.right
                    if cursor.right:
                        cursor.right.left = cursor

                max_node.left, max_node.right = None, None
                if not cursor.child:
                    cursor.child = max_node
                else:
                    cursor_child = cursor.child
                    while cursor_child.right:
                        cursor_child = cursor_child.right
                    max_node.left = cursor_child
                    cursor_child.right = max_node
                    cursor_child.right.left = cursor_child
                cursor.depth += 1
            if self.__min.value > cursor.value:
                self.__min = cursor
            print(cursor.value, end=": ")
            self.check()
            cursor = cursor.right
        return pop_value

    def __iadd__(self, other: FibHeap):
        other = copy.deepcopy(other)
        if self.__is_empty:
            self.__min = other.__min
            self.__is_empty = False
            return self
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
    heap1 = FibHeap(5, 1, 3, 2, 4, 0, 8)
    heap1 += FibHeap(7) + FibHeap(6)
    heap1.check()
    print(f"deleted: min={heap1.pop()}")
    print(f"deleted: min={heap1.pop()}")


if __name__ == '__main__':
    main()
