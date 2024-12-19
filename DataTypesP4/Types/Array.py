# Implementation on Array Data Structure

class Array:
    """A class to represent a fixed-size array."""

    def __init__(self, size):
        """Initialize the array with a specific size."""
        self.arr = [None] * size  # Fixed-size array initialized with None
        self.size = size

    def access(self, index):
        """Access an element by index."""
        if 0 <= index < self.size:
            return self.arr[index]
        else:
            raise IndexError("Index out of bounds.")

    def insert(self, index, value):
        """Insert an element at a given index."""
        if 0 <= index < self.size:
            self.arr[index] = value
        else:
            raise IndexError("Index out of bounds.")

    def delete(self, index):
        """Delete an element at a given index."""
        if 0 <= index < self.size:
            self.arr[index] = None
        else:
            raise IndexError("Index out of bounds.")

    def search(self, value):
        """Search for an element in the array."""
        try:
            return self.arr.index(value)
        except ValueError:
            return -1

    def print_array(self):
        """Print the current state of the array."""
        print(self.arr)


# Test Cases for the Array Class

def test_array():
    print("\n# TEST CASES")

    # Create an array with a specific size
    print("Creating an array of size 5...")
    array = Array(5)
    array.print_array()


    # Insert elements at different positions
    print("\nInserting elements...")
    array.insert(0, 10)
    array.insert(1, 20)
    array.insert(2, 30)
    array.print_array()

    # Delete elements from different positions
    print("\nDeleting element at index 1...")
    array.delete(1)
    array.print_array()

    # Search for existing and non-existing elements
    print("\nSearching for element 30 (Existing Element)")
    print("Found at index:", array.search(30))
    print("\nSearching for element 40 (Non-Existing Element)")
    print("Found at index:", array.search(40))

    # Print the final array
    print("\nFinal array state:")
    array.print_array()


if __name__ == "__main__":
    test_array()
