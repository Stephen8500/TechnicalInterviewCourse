class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    
    def reverseLL(self):
        current = self.head
        prev = None
        temp_next = None
        while (current):
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        self.head = prev

    def deleteNode(self, key):
        # start with head
        current = self.head

        # checks if head is the key
        if (current):
            if current.data == key:
                self.head = current.next
                current = None
                return
        
        # finds the node that needs to be deleted
        while (current):
            if current.data == key:
                break
            prev = current
            current = current.next
        
        # if the key isn't in the linked list
        if (current == None):
            return
        
        # link previous node to next node
        prev.next = current.next

        # remove node to be deleted
        current = None

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

print()

LL.deleteNode(5)
LL.printLL()
