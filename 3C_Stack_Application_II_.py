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


# Application 2: Backtracking (simple example using recursion)
def backtrack(stack, n):
    # Base case: If n is 0, print and return
    if n == 0:
        print("Reached base case:", stack.stack)
        return

    # Push the current number to the stack
    stack.push(n)
    print(f"Pushed {n} to stack")
   
    # Recursive call for backtracking
    backtrack(stack, n - 1)

    # After recursion, pop the element for backtracking
    print(f"Popped {stack.pop()} from stack")


# Example Usage for Application 2 (Backtracking)
if __name__ == "__main__":
    print("Backtracking example:")
    stack = Stack()
    
    # Backtracking with n = 3
    backtrack(stack, 3)



# Explanation:
    # Backtracking: This function uses recursion to simulate the backtracking process. It first pushes numbers onto the stack from n down to 1. After reaching the base case (n == 0), the function backtracks by popping the numbers off the stack one by one.

    # Test Data: In the example usage, we are calling backtrack(stack, 3), which will:

    # Push 3, then 2, then 1 onto the stack.
    # Once it hits the base case (n == 0), it prints the stack contents.
    # It then backtracks by popping 1, then 2, then 3 off the stack in reverse order.



#Output
    # Backtracking example:
    # Pushed 3 to stack
    # Pushed 2 to stack
    # Pushed 1 to stack
    # Reached base case: [3, 2, 1]
    # Popped 1 from stack
    # Popped 2 from stack
    # Popped 3 from stack
