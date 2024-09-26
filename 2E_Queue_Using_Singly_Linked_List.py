class QueueUsingLL:
    def __init__(self):
        self.queue = SinglyLinkedList()

    def enqueue(self, data):
        self.queue.insert_at_end(data)

    def dequeue(self):
        if self.queue.head is None:
            return "Queue is empty"
        dequeue_data = self.queue.head.data
        self.queue.delete_by_value(dequeue_data)
        return dequeue_data

    def display(self):
        self.queue.traverse()

# Example usage of Queue
queue = QueueUsingLL()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

print("Dequeued:", queue.dequeue())
queue.display()
