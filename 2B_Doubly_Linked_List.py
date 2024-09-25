# Doubly Linked List Node
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    # Delete a node by value
    def delete_by_value(self, data):
        current = self.head

        # If the head needs to be removed
        if current and current.data == data:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            current = None
            return

        while current and current.data != data:
            current = current.next

        # If data was not found
        if current is None:
            print(f"Node with data {data} not found.")
            return

        # Update next and prev pointers
        if current.next is not None:
            current.next.prev = current.prev
        if current.prev is not None:
            current.prev.next = current.next

        current = None

    # Traversal from head to end
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Traversal from end to head
    def traverse_backward(self):
        current = self.head
        if current is None:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Example usage of Doubly Linked List
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.traverse_forward()

dll.delete_by_value(20)
dll.traverse_forward()

dll.traverse_backward()


# **********************************************

# Output:
# ----------------------------------------
# | 10 -> 20 -> 30 -> None               |  
# | 10 -> 30 -> None                     |
# | 30 -> 10 -> None                     |
# ----------------------------------------

# Explanation:
# insert_at_beginning: Adds a new node at the beginning of the list.
# insert_at_end: Adds a new node at the end of the list.
# delete_by_value: Deletes a node by its value.
# traverse_forward: Traverses the list from the beginning.
# traverse_backward: Traverses the list from the end.