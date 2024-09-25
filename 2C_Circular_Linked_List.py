# Circular Singly Linked List Node
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Singly Linked List Class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_at_end(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Delete a node by value
    def delete_by_value(self, data):
        if self.head is None:
            return

        current = self.head
        prev = None

        # If the node to be deleted is the head
        if current.data == data:
            while current.next != self.head:
                current = current.next
            if self.head == current:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        while current.next != self.head and current.data != data:
            prev = current
            current = current.next

        if current.data == data:
            prev.next = current.next

    # Traversal
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage of Circular Linked List
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.traverse()

cll.delete_by_value(20)
cll.traverse()


# ****************************************************

# Output:
# ----------------------------------------
# | 10 -> 20 -> 30 ->                    |
# | 10 -> 30 ->                          |
# ----------------------------------------

# Explanation:
# insert_at_end: Adds a node to the circular list at the end.
# delete_by_value: Deletes a node from the circular list.
# traverse: Traverses the circular list and prints all nodes.