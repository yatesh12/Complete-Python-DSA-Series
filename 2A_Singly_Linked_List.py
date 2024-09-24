# Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert after a specific node
    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if current is None:
            print(f"Node with data {prev_node_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # Delete a node by value
    def delete_by_value(self, data):
        current = self.head

        # If the head needs to be removed
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # If data was not found
        if current is None:
            print(f"Node with data {data} not found.")
            return

        prev.next = current.next
        current = None

    # Traversal
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage of Singly Linked List
sll = SinglyLinkedList()
sll.insert_at_beginning(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_after(20, 25)
sll.traverse()

sll.delete_by_value(20)
sll.traverse()

# *********************************************

# Output:
# ----------------------------------------
# |  10 -> 20 -> 25 -> 30 -> None         |
# |  10 -> 25 -> 30 -> None               |
# ----------------------------------------

# Explanation:
# insert_at_beginning: Adds a new node at the beginning of the list.
# insert_at_end: Adds a new node at the end of the list.
# insert_after: Inserts a new node after a given node.
# delete_by_value: Deletes a node by its value.
# traverse: Traverses and prints all the elements in the list.
