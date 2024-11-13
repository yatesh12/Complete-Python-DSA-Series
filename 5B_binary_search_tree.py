# binary_search_tree.py

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)
        print(f"Inserted {data} into the BST.")

    def _insert_recursive(self, node, data):
        if node is None:
            return BSTNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

    def search(self, data):
        result = self._search_recursive(self.root, data)
        print(f"Search for {data}: {'Found' if result else 'Not Found'}")
        return result

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(3)
    bst.insert(7)
    bst.insert(15)

    print("\nIn-Order Traversal of BST:")
    bst.in_order_traversal(bst.root)

    print("\n")
    bst.search(7)
    bst.search(8)
