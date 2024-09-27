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


# Application 1: Check if parentheses are balanced
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":  # If it's an opening bracket, push it onto the stack
            stack.push(char)
        elif char in ")}]":  # If it's a closing bracket
            if stack.is_empty():  # No matching opening bracket
                return False
            top = stack.pop()  # Pop the last opening bracket
            if not is_matching(top, char):  # Check if it matches
                return False
    return stack.is_empty()  # In the end, the stack should be empty if balanced


# Helper function to check if the parentheses match
def is_matching(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')


# Test cases
expressions = [
    "((()))",  # Balanced
    "[(])",    # Not balanced
    "{[()]}",  # Balanced
    "[{()}]",  # Balanced
    "([)]",    # Not balanced
    "{}",      # Balanced
    "(]",      # Not balanced
    "[()]{}{[()()]()}",  # Balanced
]

# Running the test cases
for expr in expressions:
    result = is_balanced(expr)
    print(f"Expression: {expr} --> Balanced: {result}")


Share


You said:
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


complete the above file with test values.
ChatGPT said:
ChatGPT
Here’s how you can complete the file with test values to test the stack implementation:

python
Copy code
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
Explanation:
This script creates an instance of the Stack class and performs various operations such as push, pop, peek, and checks if the stack is empty.
It also prints the current state of the stack at different stages to verify that the implementation works as expected.
When you run this script, it should output the following:

vbnet
Copy code
Is the stack empty? True
Stack from bottom to top: [10, 20, 30]
Size of the stack: 3
Top element (peek): 30
Popped element: 30
Popped element: 20
Stack from bottom to top: [10]
Size of the stack: 1
Top element (peek): 10
Popped element: 10
Popped element: Stack is empty
Is the stack empty? True
Stack from bottom to top: []





You said:
# Application 1: Check if parentheses are balanced
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if not is_matching(top, char):
                return False
    return stack.is_empty()

# Helper function to check if the parentheses match
def is_matching(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')



this also
ChatGPT said:
ChatGPT
To complete the file with test cases for checking if parentheses are balanced, here's how you can integrate it with the Stack class and provide some sample test values:

python
Copy code
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


# Application 1: Check if parentheses are balanced
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":  # If it's an opening bracket, push it onto the stack
            stack.push(char)
        elif char in ")}]":  # If it's a closing bracket
            if stack.is_empty():  # No matching opening bracket
                return False
            top = stack.pop()  # Pop the last opening bracket
            if not is_matching(top, char):  # Check if it matches
                return False
    return stack.is_empty()  # In the end, the stack should be empty if balanced


# Helper function to check if the parentheses match
def is_matching(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')


# Test cases
expressions = [
    "((()))",  # Balanced
    "[(])",    # Not balanced
    "{[()]}",  # Balanced
    "[{()}]",  # Balanced
    "([)]",    # Not balanced
    "{}",      # Balanced
    "(]",      # Not balanced
    "[()]{}{[()()]()}",  # Balanced
]

# Running the test cases
for expr in expressions:
    result = is_balanced(expr)
    print(f"Expression: {expr} --> Balanced: {result}")


# Explanation:
    # Stack operations: The Stack class is used to manage opening brackets. For every closing bracket encountered, it checks if the top of the stack has a matching opening bracket.
    # is_balanced function: It iterates over the expression, pushing opening brackets onto the stack and popping them when encountering closing brackets. If the brackets don't match or the stack isn't empty at the end, the expression is not balanced.
    # Test cases: A series of expressions are tested to check if parentheses are balanced.


# Output:
    # Expression: ((())) --> Balanced: True
    # Expression: [(]) --> Balanced: False
    # Expression: {[()]} --> Balanced: True
    # Expression: [{()}] --> Balanced: True
    # Expression: ([)] --> Balanced: False
    # Expression: {} --> Balanced: True
    # Expression: (] --> Balanced: False
    # Expression: [()]{}{[()()]()} --> Balanced: True
    