# basic_tree_structure.py

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert_left(self, current_node, data):
        if current_node.left is None:
            current_node.left = TreeNode(data)
        else:
            new_node = TreeNode(data)
            new_node.left = current_node.left
            current_node.left = new_node
        print(f"Inserted {data} to the left of {current_node.data}")

    def insert_right(self, current_node, data):
        if current_node.right is None:
            current_node.right = TreeNode(data)
        else:
            new_node = TreeNode(data)
            new_node.right = current_node.right
            current_node.right = new_node
        print(f"Inserted {data} to the right of {current_node.data}")

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

# Example usage
if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert_left(tree.root, 5)
    tree.insert_right(tree.root, 15)
    tree.insert_left(tree.root.left, 3)
    tree.insert_right(tree.root.left, 7)

    print("\nIn-Order Traversal:")
    tree.in_order_traversal(tree.root)

    print("\n\nPre-Order Traversal:")
    tree.pre_order_traversal(tree.root)

    print("\n\nPost-Order Traversal:")
    tree.post_order_traversal(tree.root)



# OUTPUT:
# Inserted 5 to the left of 10
# Inserted 15 to the right of 10
# Inserted 3 to the left of 5
# Inserted 7 to the right of 5

# In-Order Traversal:
# 3 5 7 10 15 

# Pre-Order Traversal:
# 10 5 3 7 15 

# Post-Order Traversal:
# 3 7 5 15 10
