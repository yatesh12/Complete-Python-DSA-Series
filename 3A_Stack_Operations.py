class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to implement stack

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Push an element to the stack
    def push(self, item):
        self.stack.append(item)

    # Pop an element from the stack (removes and returns the top element)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    # Peek at the top element of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Print the stack (from bottom to top)
    def print_stack(self):
        print("Stack from bottom to top:", self.stack)


# Test the Stack implementation
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    # Test if the stack is empty
    print("Is the stack empty?", stack.is_empty())  # Expected: True

    # Push elements to the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Print the stack
    stack.print_stack()  # Expected: Stack from bottom to top: [10, 20, 30]

    # Check the size of the stack
    print("Size of the stack:", stack.size())  # Expected: 3

    # Peek at the top element
    print("Top element (peek):", stack.peek())  # Expected: 30

    # Pop elements from the stack
    print("Popped element:", stack.pop())  # Expected: 30
    print("Popped element:", stack.pop())  # Expected: 20

    # Print the stack after popping
    stack.print_stack()  # Expected: Stack from bottom to top: [10]

    # Check the size of the stack after popping
    print("Size of the stack:", stack.size())  # Expected: 1

    # Peek at the top element after popping
    print("Top element (peek):", stack.peek())  # Expected: 10

    # Pop the last element
    print("Popped element:", stack.pop())  # Expected: 10

    # Try popping from an empty stack
    print("Popped element:", stack.pop())  # Expected: "Stack is empty"

    # Check if the stack is empty after popping all elements
    print("Is the stack empty?", stack.is_empty())  # Expected: True

    # Print the empty stack
    stack.print_stack()  # Expected: Stack from bottom to top: []


# Explanation:
    # This script creates an instance of the Stack class and performs various operations such as push, pop, peek, and checks if the stack is empty.
    # It also prints the current state of the stack at different stages to verify that the implementation works as expected.


#Output:
    # Is the stack empty? True
    # Stack from bottom to top: [10, 20, 30]
    # Size of the stack: 3
    # Top element (peek): 30
    # Popped element: 30
    # Popped element: 20
    # Stack from bottom to top: [10]
    # Size of the stack: 1
    # Top element (peek): 10
    # Popped element: 10
    # Popped element: Stack is empty
    # Is the stack empty? True
    # Stack from bottom to top: []
    