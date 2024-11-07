
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        heapq.heappush(self.queue, (priority, item))
        print(f"Enqueued (priority: {priority}, item: {item}) -> Queue: {self.queue}")

    def dequeue(self):
        if not self.queue:
            print("[Error] Queue is empty. Cannot dequeue.")
            return
        item = heapq.heappop(self.queue)[1]
        print(f"Dequeued item with highest priority: {item} -> Queue: {self.queue}")
        return item

    def peek(self):
        if not self.queue:
            print("[Error] Queue is empty. Cannot peek.")
            return
        item = self.queue[0][1]
        print(f"Peeked at item with highest priority: {item}")
        return item

    def is_empty(self):
        return not self.queue

# Example usage of PriorityQueue
if __name__ == "__main__":
    pq = PriorityQueue()
    print("\n== Priority Queue Operations ==")

    # Enqueue items with different priorities
    pq.enqueue(2, "Clean the house")
    pq.enqueue(1, "Finish homework")
    pq.enqueue(3, "Go shopping")

    # Peek at the item with the highest priority
    pq.peek()

    # Dequeue items
    pq.dequeue()
    pq.dequeue()

    # Check if queue is empty
    print("\nIs queue empty?", pq.is_empty())


#OUTPUT:J

# == Priority Queue Operations ==
# Enqueued (priority: 2, item: Clean the house) -> Queue: [(2, 'Clean the house')]
# Enqueued (priority: 1, item: Finish homework) -> Queue: [(1, 'Finish homework'), (2, 'Clean the house')]
# Enqueued (priority: 3, item: Go shopping) -> Queue: [(1, 'Finish homework'), (2, 'Clean the house'), (3, 'Go shopping')]

# Peeked at item with highest

