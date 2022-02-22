class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        
    def print(self):
        if self.head:
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def deleteNode(self, key):
        if self.head:
            current = self.head
            prev = None

            if current.data == key:
                self.head = current.next
                current = None
                return

            while current:
                if current.data == key:
                    break
                prev = current
                current = current.next
            
            if current == None:
                return
            
            prev.next = current.next

            current = None

    def reverse(self):
        if self.head:
            current = self.head
            next = None
            prev = None

            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            
            self.head = prev

# test code
firstList = LL()
firstList.insert(3)
firstList.insert(4)
firstList.insert(5)
firstList.insert(6)
firstList.insert(7)
firstList.insert(8)
firstList.print()
print("Delete 6:")
firstList.deleteNode(6)
firstList.print()
print("Reverse List:")
firstList.reverse()
firstList.print()
