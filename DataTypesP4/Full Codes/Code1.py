import sys
from typing import Any, Optional

# -----------------------------
# Array Implementation
# -----------------------------
class Array:
    def __init__(self, size: int):
        self.arr = [None] * size  # Fixed-size array initialized with None
        self.size = size

    def access(self, index: int) -> Any:
        if 0 <= index < self.size:
            return self.arr[index]
        else:
            raise IndexError("Index out of bounds.")

    def insert(self, index: int, value: Any):
        if 0 <= index < self.size:
            self.arr[index] = value
        else:
            raise IndexError("Index out of bounds.")

    def delete(self, index: int):
        if 0 <= index < self.size:
            self.arr[index] = None
        else:
            raise IndexError("Index out of bounds.")

    def search(self, value: Any) -> int:
        try:
            return self.arr.index(value)
        except ValueError:
            return -1

# -----------------------------
# Binary Search Tree (BST) Implementation
# -----------------------------
class BSTNode:
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BST:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: int, value: Any):
        def _insert(node: Optional[BSTNode], key: int, value: Any) -> BSTNode:
            if node is None:
                return BSTNode(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            return node

        self.root = _insert(self.root, key, value)

    def search(self, key: int) -> Any:
        def _search(node: Optional[BSTNode], key: int) -> Any:
            if node is None:
                return None
            if key == node.key:
                return node.value
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

    def inorder(self):
        result = []
        def _inorder(node: Optional[BSTNode]):
            if node:
                _inorder(node.left)
                result.append((node.key, node.value))
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self):
        result = []
        def _preorder(node: Optional[BSTNode]):
            if node:
                result.append((node.key, node.value))
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self):
        result = []
        def _postorder(node: Optional[BSTNode]):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append((node.key, node.value))
        _postorder(self.root)
        return result

# -----------------------------
# Union Operations Using Sets
# -----------------------------
class UnionOperations:
    def __init__(self, set_a: set, set_b: set):
        self.set_a = set_a
        self.set_b = set_b

    def union(self) -> set:
        return self.set_a | self.set_b

    def intersection(self) -> set:
        return self.set_a & self.set_b

    def difference(self) -> set:
        return self.set_a - self.set_b

    def is_member(self, value: Any) -> bool:
        return value in self.set_a or value in self.set_b

# -----------------------------
# Linked List Implementation
# -----------------------------
class LinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['LinkedListNode'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[LinkedListNode] = None

    def insert(self, data: Any):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key: Any):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            if prev:
                prev.next = temp.next
            else:
                self.head = temp.next

    def search(self, key: Any) -> bool:
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def traverse(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

# -----------------------------
# Record Implementation (Person Class)
# -----------------------------
class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

# -----------------------------
# Pointers in Python Using Object References
# -----------------------------
# Demonstrated within the Linked List class (references used for 'next').

# -----------------------------
# Testing the Data Structures
# -----------------------------
def main():
    print("\n# ARRAY TEST")
    array = Array(5)
    array.insert(0, 10)
    array.insert(1, 20)
    print("Access index 0:", array.access(0))
    print("Search 20:", array.search(20))
    array.delete(1)
    print("After deletion at index 1:", array.arr)

    print("\n# BST TEST")
    bst = BST()
    bst.insert(10, "Value10")
    bst.insert(5, "Value5")
    bst.insert(15, "Value15")
    print("Inorder traversal:", bst.inorder())
    print("Search key 15:", bst.search(15))

    print("\n# UNION TEST")
    sets = UnionOperations({1, 2, 3}, {3, 4, 5})
    print("Union:", sets.union())
    print("Intersection:", sets.intersection())
    print("Difference:", sets.difference())

    print("\n# LINKED LIST TEST")
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    print("Traverse:", linked_list.traverse())
    linked_list.delete(2)
    print("After deletion:", linked_list.traverse())

    print("\n# RECORD TEST")
    person = Person("John Doe", 25, "123 Street")
    print(person.display())

if __name__ == "__main__":
    main()
