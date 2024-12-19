import typing
from typing import Any, Optional, Generic, TypeVar, List
import unittest


# 1. Arrays Implementation
class DynamicArray:
    """
    A custom implementation of a dynamic array with basic operations.
    Provides similar functionality to built-in lists with explicit methods.
    """

    def __init__(self, initial_capacity: int = 10):
        """
        Initialize the dynamic array with a given initial capacity.

        :param initial_capacity: Starting size of the internal array
        """
        self._data = [None] * initial_capacity
        self._size = 0
        self._capacity = initial_capacity

    def __len__(self) -> int:
        """Return the number of elements in the array."""
        return self._size

    def __getitem__(self, index: int) -> Any:
        """
        Access element at a specific index.

        :param index: Index of the element to retrieve
        :return: Element at the specified index
        :raises IndexError: If index is out of bounds
        """
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError("Index out of bounds")

    def append(self, item: Any) -> None:
        """
        Add an element to the end of the array.
        Resize the array if capacity is exceeded.

        :param item: Element to be added
        """
        if self._size == self._capacity:
            # Double the capacity when array is full
            self._resize(2 * self._capacity)

        self._data[self._size] = item
        self._size += 1

    def insert(self, index: int, item: Any) -> None:
        """
        Insert an element at a specific index.

        :param index: Position to insert the element
        :param item: Element to be inserted
        :raises IndexError: If index is out of bounds
        """
        if 0 <= index <= self._size:
            # Shift elements to make space
            for i in range(self._size, index, -1):
                self._data[i] = self._data[i - 1]

            self._data[index] = item
            self._size += 1
        else:
            raise IndexError("Index out of bounds")

    def delete(self, index: int) -> Any:
        """
        Remove and return an element at a specific index.

        :param index: Position of element to remove
        :return: Removed element
        :raises IndexError: If index is out of bounds
        """
        if 0 <= index < self._size:
            item = self._data[index]

            # Shift elements to fill the gap
            for i in range(index, self._size - 1):
                self._data[i] = self._data[i + 1]

            self._size -= 1
            return item

        raise IndexError("Index out of bounds")

    def _resize(self, new_capacity: int) -> None:
        """
        Resize the internal array to a new capacity.

        :param new_capacity: New size of the array
        """
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity


# 2. Binary Search Tree Implementation
class TreeNode:
    """Represents a node in a Binary Search Tree."""

    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    """Implements a Binary Search Tree with various traversal methods."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair into the BST.

        :param key: Key to be inserted
        :param value: Corresponding value
        """
        self.root = self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node: Optional[TreeNode], key: Any, value: Any) -> TreeNode:
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            node.value = value  # Update value if key exists

        return node

    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a value by key.

        :param key: Key to search for
        :return: Value associated with the key or None
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Optional[TreeNode], key: Any) -> Optional[Any]:
        if node is None or node.key == key:
            return node.value if node else None

        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self) -> List[Any]:
        """Perform an inorder traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)


# 3. Union Data Structure
T = TypeVar('T')


class UnionSet(Generic[T]):
    """
    Implements a set-like data structure with union operations.
    Uses a dictionary for efficient storage and lookup.
    """

    def __init__(self):
        self._data: typing.Dict[T, bool] = {}

    def add(self, item: T) -> None:
        """Add an item to the set."""
        self._data[item] = True

    def remove(self, item: T) -> None:
        """Remove an item from the set."""
        self._data.pop(item, None)

    def __contains__(self, item: T) -> bool:
        """Check if an item is in the set."""
        return item in self._data

    def union(self, other: 'UnionSet[T]') -> 'UnionSet[T]':
        """Perform a union operation with another set."""
        result = UnionSet[T]()
        for item in self._data:
            result.add(item)
        for item in other._data:
            result.add(item)
        return result

    def intersection(self, other: 'UnionSet[T]') -> 'UnionSet[T]':
        """Perform an intersection operation with another set."""
        result = UnionSet[T]()
        for item in self._data:
            if item in other:
                result.add(item)
        return result


# 4. Linked List Implementation
class LinkedListNode:
    """Represents a node in a Linked List."""

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[LinkedListNode] = None


class LinkedList:
    """Implements a singly linked list with basic operations."""

    def __init__(self):
        self.head: Optional[LinkedListNode] = None

    def insert_front(self, data: Any) -> None:
        """Insert a new node at the front of the list."""
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data: Any) -> bool:
        """
        Delete the first occurrence of a node with given data.

        :return: True if deleted, False if not found
        """
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, data: Any) -> bool:
        """Check if a value exists in the linked list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# 5. Record/Person Class
class Person:
    """
    Represents a person with basic attributes.
    Demonstrates object-oriented record implementation.
    """

    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self) -> str:
        """String representation of the person."""
        return f"{self.name} (Age: {self.age}, Address: {self.address})"


# 6. Pointer Demonstration
def pointer_demo() -> None:
    """
    Demonstrate pointer-like behavior in Python using object references.
    Uses a linked list to illustrate reference manipulation.
    """

    class PointerNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    # Create nodes
    node1 = PointerNode(10)
    node2 = PointerNode(20)
    node3 = PointerNode(30)

    # Link nodes (simulate pointer behavior)
    node1.next = node2
    node2.next = node3

    # Traverse using references
    current = node1
    while current:
        print(current.data, end=" ")
        current = current.next


# Comprehensive Unit Testing
class DataStructuresTest(unittest.TestCase):
    def test_dynamic_array(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.insert(1, 3)

        self.assertEqual(len(arr), 3)
        self.assertEqual(arr[1], 3)
        self.assertEqual(arr.delete(1), 3)

    def test_binary_search_tree(self):
        bst = BinarySearchTree()
        bst.insert(5, "Five")
        bst.insert(3, "Three")
        bst.insert(7, "Seven")

        self.assertEqual(bst.search(5), "Five")
        self.assertEqual(bst.inorder_traversal(), [(3, "Three"), (5, "Five"), (7, "Seven")])

    def test_union_set(self):
        set1 = UnionSet[int]()
        set1.add(1)
        set1.add(2)

        set2 = UnionSet[int]()
        set2.add(2)
        set2.add(3)

        union_set = set1.union(set2)
        self.assertTrue(1 in union_set)
        self.assertTrue(2 in union_set)
        self.assertTrue(3 in union_set)

    def test_linked_list(self):
        ll = LinkedList()
        ll.insert_front(1)
        ll.insert_front(2)

        self.assertTrue(ll.search(1))
        self.assertTrue(ll.delete(1))
        self.assertFalse(ll.search(1))

    def test_person(self):
        person = Person("Alice", 30, "123 Main St")
        self.assertEqual(str(person), "Alice (Age: 30, Address: 123 Main St)")


def main():
    # Demonstrate data structures
    print("Data Structures Demonstration")

    # Dynamic Array
    print("\nDynamic Array:")
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    print(f"Array elements: {[arr[i] for i in range(len(arr))]}")

    # Binary Search Tree
    print("\nBinary Search Tree:")
    bst = BinarySearchTree()
    bst.insert(5, "Five")
    bst.insert(3, "Three")
    bst.insert(7, "Seven")
    print(f"Tree traversal: {bst.inorder_traversal()}")

    # Pointer Demonstration
    print("\nPointer Demonstration:")
    pointer_demo()


if __name__ == "__main__":
    main()
    # Uncomment the line below to run unit tests
    unittest.main()