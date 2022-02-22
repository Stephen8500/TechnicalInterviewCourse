class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head:
            current = self.head
            while current:
                print(current.data)
                current = current.next
            
    def insert(self, data):
        newNode = Node(data)
        
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        
    def delete(self, key):
        if self.head:
            current = self.head
            if current == key:
                self.head = current.next
                current = None
                return
            
            prev = None
            while current:
                if current.data == key:
                    break   
                prev = current
                current = current.next 
                
            if current == None:
                return("not found")
            
            prev.next = current.next
            current = None

    def reverse(self):
        if self.head:
            current = self.head
            prev = None
            next = None

            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next

            self.head = prev
                

ll = LinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.print()
print()
ll.delete(6)
ll.print()
print()
ll.reverse()
ll.print()

