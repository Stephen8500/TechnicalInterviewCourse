class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert method
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def reverseLL(self):
        current = self.head
        temp_next = None
        temp_previous = None
        while (current):
            temp_next = current.next
            current.next = temp_previous
            temp_previous = current
            current = temp_next
        self.head = temp_previous

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.insert(7)

LL.printLL()

print()

LL.reverseLL()
LL.printLL()