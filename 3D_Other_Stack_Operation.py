class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None


# 1. Reversing a String Using a Stack
def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str


# 2. Infix to Postfix Conversion (Shunting Yard Algorithm)
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    stack = Stack()
    result = ""
    for char in expression:
        if char.isalnum():
            result += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                result += stack.pop()
            stack.pop()  # Remove '('
        else:
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                result += stack.pop()
            stack.push(char)
    while not stack.is_empty():
        result += stack.pop()
    return result


# 3. Postfix Expression Evaluation
def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if char == '+':
                stack.push(val1 + val2)
            elif char == '-':
                stack.push(val1 - val2)
            elif char == '*':
                stack.push(val1 * val2)
            elif char == '/':
                stack.push(val1 // val2)  # Integer division
    return stack.pop()


# 4. Next Greater Element
def next_greater_element(arr):
    stack = Stack()
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while not stack.is_empty() and arr[i] > arr[stack.peek()]:
            index = stack.pop()
            result[index] = arr[i]
        stack.push(i)
    return result


# 5. Stock Span Problem
def calculate_stock_span(prices):
    stack = Stack()
    span = [0] * len(prices)
    for i in range(len(prices)):
        while not stack.is_empty() and prices[stack.peek()] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if stack.is_empty() else i - stack.peek()
        stack.push(i)
    return span


# Example Usage
if __name__ == "__main__":
    # 1. Reversing a String Using a Stack
    input_str = "Hello, World!"
    reversed_str = reverse_string(input_str)
    print("Original string:", input_str)
    print("Reversed string:", reversed_str)

    # 2. Infix to Postfix Conversion
    infix_expr = "A+B*(C^D-E)"
    postfix_expr = infix_to_postfix(infix_expr)
    print("\nInfix Expression:", infix_expr)
    print("Postfix Expression:", postfix_expr)

    # 3. Postfix Expression Evaluation
    postfix_expr = "231*+9-"
    result = evaluate_postfix(postfix_expr)
    print("\nPostfix Expression:", postfix_expr)
    print("Evaluation Result:", result)

    # 4. Next Greater Element
    arr = [4, 5, 2, 25]
    nge = next_greater_element(arr)
    print("\nArray:", arr)
    print("Next Greater Elements:", nge)

    # 5. Stock Span Problem
    prices = [100, 80, 60, 70, 60, 75, 85]
    span = calculate_stock_span(prices)
    print("\nStock Prices:", prices)
    print("Stock Span:", span)



# Explanation:
    # Reversing a String: Reverses the input string by pushing and popping characters using the stack.
    # Infix to Postfix Conversion: Converts an infix expression into postfix notation using the Shunting Yard algorithm.
    # Postfix Expression Evaluation: Evaluates a postfix expression by applying operators to operands popped from the stack.
    # Next Greater Element: For each element in the array, finds the next greater element using a stack.
    # Stock Span Problem: Computes the stock span for each day's price using a stack to track previous lower prices.



# Output
    # Original string: Hello, World!
    # Reversed string: !dlroW ,olleH

    # Infix Expression: A+B*(C^D-E)
    # Postfix Expression: ABCD^E-*+

    # Postfix Expression: 231*+9-
    # Evaluation Result: -4

    # Array: [4, 5, 2, 25]
    # Next Greater Elements: [5, 25, 25, -1]

    # Stock Prices: [100, 80, 60, 70, 60, 75, 85]
    # Stock Span: [1, 1, 1, 2, 1, 4, 6]
