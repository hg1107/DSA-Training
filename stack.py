'''

Stack using array(list): Easy to implement
                         Lags when large data

Stack using linked list: More efficient for large data
                         Hard to implement

'''


import sys

class Stack:
    # Constructor for creating and initiating memory
    def __init__(self, stackSize): 
        self.stackSize = stackSize
        self.stack = [] # Stack has initialized

    # isFull operation to check if stack is full or not
    def isFull(self):
        if len(self.stack) == self.stackSize: 
            return True 
        else:
            return False

    # isEmpty operation to check if stack is empty or not
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    # Push operation to add value to stack
    def push(self, value):
        if self.isFull():
            print("Stack is full. Cannot push value.")
        else:
            self.stack.append(value)
            print(f"Pushed {value} to stack.")

    # Pop operation to remove value from stack
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop value.")
        else:
            value = self.stack.pop()
            print(f"Popped {value} from stack.")

    # Peek operation to view the top value of stack
    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Cannot peek value.")
        else:
            value = self.stack[-1]
            print(f"Top value of stack is {value}.")

    # Delete stack
    def delete(self):
        self.stack = None
        print("Stack has been deleted")

    # Display Stack
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stack)


size = int(input("Enter the size of stack: "))
obj = Stack(size) # Object of class Stack

# While loop to run it infinitely until user wants to exit
while True:
    print("1. Push operation")
    print("2. Pop operation")
    print("3. Peek operation")
    print("4. isEmpty operation")
    print("5. isFull operation")
    print("6. Delete stack operation")
    print("7. Display stack operation")
    print("8. exit operation")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to be pushed: "))
        obj.push(value)
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        print(obj.isEmpty())
    elif choice == 5:
        print(obj.isFull)
    elif choice == 6:
        obj.delete()
    elif choice == 7:
        obj.display()
    elif choice == 8:
        sys.exit()