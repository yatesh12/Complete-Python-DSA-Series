# tree_traversals.py
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeTraversals:
    def level_order_traversal(self, root):
        if root is None:
            return
        queue = deque([root])
        print("Level Order Traversal:", end=" ")
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def depth_first_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.depth_first_traversal(node.left)
            self.depth_first_traversal(node.right)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    traversals = TreeTraversals()

    print("\nLevel-Order Traversal:")
    traversals.level_order_traversal(root)

    print("\nDepth-First Traversal:")
    traversals.depth_first_traversal(root)
