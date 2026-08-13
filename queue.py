'''

FIFO

Implementation: 1. Python list -  queue without capacity
                                  queue with capacity
                2. Linked list

'''

import sys

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []  

    def ifFull(self):
        if len(self.queue) == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.ifFull():
            print("Queue is full. Cannot enqueue.")
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
        else:
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")

    def peekFront(self):
        if self.isEmpty():
            print("Queue is empty. No front item.")
        else:
            print(f"Front item: {self.queue[0]}")

    def deleteQueue(self):
        self.queue = []
        print("Queue deleted.")

    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Queue contents:", self.queue)


size = int(input("Enter the size of the queue: "))
obj = Queue(size)

while True:
    print("1. Enqueue Operation")
    print("2. Dequeue Operation")
    print("3. PeekFront Operation")
    print("4. isEmpty Operation")
    print("5. isFull Operation")
    print("6. Delete entire Queue")
    print("7. Display Operation")
    print("8. Exit Operation")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to enqueue: ")
        obj.enqueue(item)
    elif choice == 2:
        obj.dequeue()
    elif choice == 3:
        obj.peekFront()
    elif choice == 4:
        print(obj.isEmpty())
    elif choice == 5:
        print(obj.ifFull())
    elif choice == 6:
        obj.deleteQueue()
    elif choice == 7:
        obj.display()
    elif choice == 8:
        print("Exiting...")
        sys.exit()