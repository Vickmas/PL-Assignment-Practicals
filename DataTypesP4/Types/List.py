class Node:
    """A class to represent a node in the singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A class to represent the entire singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        """Insert a node at a specific position in the linked list."""
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of bounds.")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        """Delete a node from the beginning of the linked list."""
        if not self.head:
            raise IndexError("List is empty.")
        self.head = self.head.next

    def delete_at_end(self):
        """Delete a node from the end of the linked list."""
        if not self.head:
            raise IndexError("List is empty.")
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        """Delete a node from a specific position in the linked list."""
        if position == 0:
            self.delete_at_beginning()
            return

        current = self.head
        for _ in range(position - 1):
            if not current or not current.next:
                raise IndexError("Position out of bounds.")
            current = current.next

        current.next = current.next.next

    def search(self, data):
        """Search for a node in the linked list by its value."""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def traverse(self):
        """Traverse the linked list and return a list of node values."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Test Cases
def test_linked_list():
    print("\n# TESTING LINKED LIST")

    ll = LinkedList()

    # Inserting nodes
    print("Inserting nodes at the beginning, end, and specific positions.")
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_position(1, 15)  # Insert 15 at position 1
    print("List after insertions:", ll.traverse())

    # Deleting nodes
    print("Deleting nodes from the beginning, end, and specific positions.")
    ll.delete_at_beginning()
    print("List after deleting from the beginning:", ll.traverse())
    ll.delete_at_end()
    print("List after deleting from the end:", ll.traverse())
    ll.delete_at_position(0)  # Delete remaining node at position 0
    print("List after deleting position 0:", ll.traverse())

    # Searching for nodes
    print("Inserting nodes for search testing.")
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    print("List before searching:", ll.traverse())
    print("Searching for 30:", ll.search(30))  # Should return position 0
    print("Searching for 50:", ll.search(50))  # Should return -1

# Execute test cases
if __name__ == "__main__":
    test_linked_list()
