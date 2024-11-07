
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove an item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """Get the item at the front without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]

    def size(self):
        """Get the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """String representation of the queue."""
        return "Queue: " + str(self.items)


# Example usage of the Queue class
if __name__ == "__main__":
    queue = Queue()
    
    # Check if the queue is initially empty
    print("Is the queue empty?", queue.is_empty())  # Output: True
    
    # Enqueue some items
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueuing 10, 20, 30:", queue)  # Output: Queue: [10, 20, 30]
    
    # Check the size of the queue
    print("Current queue size:", queue.size())  # Output: 3
    
    # Peek at the front item
    print("Item at the front:", queue.peek())  # Output: 10
    
    # Dequeue an item
    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)  # Output: 10
    print("Queue after dequeuing an item:", queue)  # Output: Queue: [20, 30]
    
    # Check if the queue is empty now
    print("Is the queue empty?", queue.is_empty())  # Output: False
    
    # Dequeue all remaining items
    queue.dequeue()
    queue.dequeue()
    print("Queue after dequeuing all items:", queue)  # Output: Queue: []
    
    # Verify that the queue is empty
    print("Is the queue empty after all dequeues?", queue.is_empty())  # Output: True
    
    # Attempt to dequeue from an empty queue to raise an exception
    try:
        queue.dequeue()
    except IndexError as e:
        print("Exception caught:", str(e))  # Output: Exception caught: Cannot dequeue from an empty queue

#OUTPUT:

# Is the queue empty? True
# Queue after enqueuing 10, 20, 30: Queue: [10, 20, 30]
# Current queue size: 3
# Item at the front: 10
# Dequeued item: 10
# Queue after dequeuing an item: Queue: [20, 30]
# Is the queue empty? False
# Queue after dequeuing all items: Queue: []
# Is the queue empty after all dequeues? True
# Exception caught: Cannot dequeue from an empty queue
