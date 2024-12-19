
# Binary Tree Implementation

class Node:
    """A class to represent a node in the binary tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    """A class to represent a binary tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the binary tree."""
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Search for a key in the binary tree."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """Perform an inorder traversal of the binary tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """Perform a preorder traversal of the binary tree."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """Perform a postorder traversal of the binary tree."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

    def height(self):
        """Find the height of the binary tree."""
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def is_balanced(self):
        """Check if the tree is balanced."""
        def check_balance(node):
            if not node:
                return 0, True
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
            return max(left_height, right_height) + 1, balanced

        _, balanced = check_balance(self.root)
        return balanced

# Test Cases for the BinaryTree Class
def test_binary_tree():
    print("\n# TESTING BINARY TREE")
    tree = BinaryTree()

    # Insert nodes
    print("Inserting nodes: 10, 5, 15, 3, 7, 18")
    for key in [10, 5, 15, 3, 7, 18]:
        tree.insert(key)

    # Traversals
    print("Inorder Traversal:", tree.inorder_traversal())
    print("Preorder Traversal:", tree.preorder_traversal())
    print("Postorder Traversal:", tree.postorder_traversal())

    # Search for nodes
    print("Searching for node 7:", tree.search(7))
    print("Searching for node 20:", tree.search(20))

    # Tree height
    print("Height of tree:", tree.height())

    # Check if the tree is balanced
    print("Is the tree balanced?:", tree.is_balanced())

# Execution
if __name__ == "__main__":
    test_binary_tree()
