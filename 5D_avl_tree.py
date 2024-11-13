# avl_tree.py

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, data):
        if root is None:
            return AVLNode(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data, end=" ")
            self.in_order_traversal(root.right)

# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    data = [10, 20, 30, 40, 50, 25]
    for value in data:
        root = avl_tree.insert(root, value)

    print("\nIn-Order Traversal of AVL Tree:")
    avl_tree.in_order_traversal(root)


# OUTPUT:

# Inserted 10 into the BST.
# Inserted 5 into the BST.
# Inserted 20 into the BST.
# Inserted 3 into the BST.
# Inserted 7 into the BST.
# Inserted 15 into the BST.

# In-Order Traversal of BST:
# 3 5 7 10 15 20

# Search for 7: Found
# Search for 8: Not Found