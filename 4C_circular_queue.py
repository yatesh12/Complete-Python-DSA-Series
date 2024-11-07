
class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_full():
            print(f"[Error] Queue is full. Cannot enqueue {item}.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        print(f"Enqueued {item} -> Queue: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            print("[Error] Queue is empty. Cannot dequeue.")
            return
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(f"Dequeued {item} -> Queue: {self.queue}")
        return item

    def peek(self):
        if self.is_empty():
            print("[Error] Queue is empty. Cannot peek.")
            return
        print(f"Peeked at front: {self.queue[self.front]}")
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        return f"Queue from front to rear: {self.queue[self.front:self.rear+1] if self.rear >= self.front else self.queue[self.front:] + self.queue[:self.rear+1]}"

# Example usage of CircularQueue
if __name__ == "__main__":
    cq = CircularQueue(5)
    print("\n== Circular Queue Operations ==")

    # Enqueue items
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)  # Queue should now be full
    cq.enqueue(6)  # Should display an error message

    print("\nQueue after enqueuing 5 items:", cq)

    # Dequeue items
    cq.dequeue()
    cq.dequeue()
    print("\nQueue after dequeuing 2 items:", cq)

    # Enqueue more items to test circular nature
    cq.enqueue(6)
    cq.enqueue(7)
    print("\nQueue after enqueuing 6 and 7:", cq)

    # Peek at the front item
    cq.peek()
    print("\nFinal Queue State:", cq)



#OUTPUT:

# == Circular Queue Operations ==
# Enqueued 1 -> Queue: [1, None, None, None, None]
# Enqueued 2 -> Queue: [1, 2, None, None, None]
# Enqueued 3 -> Queue: [1, 2, 3, None, None]
# Enqueued 4 -> Queue: [1, 2, 3, 4, None]
# Enqueued 5 -> Queue: [1, 2, 3, 4, 5]
# [Error] Queue is full. Cannot enqueue 6.

# Queue after enqueuing 5 items: Queue from front to rear: [1, 2, 3, 4, 5]

# Dequeued 1 -> Queue: [1, 2, 3, 4, 5]
# Dequeued 2 -> Queue: [1, 2, 3, 4, 5]

# Queue after dequeuing 2 items: Queue from front to rear: [3, 4, 5]

# Enqueued 6 -> Queue: [6, 2, 3, 4, 5]
# Enqueued 7 -> Queue: [6, 7, 3, 4, 5]

# Queue after enqueuing 6 and 7: Queue from front to rear: [3, 4, 5, 6, 7]

# Peeked at front: 3

# Final Queue State: Queue from front to rear: [3, 4, 5, 6, 7]

