class StackUsingLL:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, data):
        self.stack.insert_at_beginning(data)

    def pop(self):
        if self.stack.head is None:
            return "Stack is empty"
        pop_data = self.stack.head.data
        self.stack.delete_by_value(pop_data)
        return pop_data

    def display(self):
        self.stack.traverse()

# Example usage of Stack
stack = StackUsingLL()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print("Popped:", stack.pop())
stack.display()


