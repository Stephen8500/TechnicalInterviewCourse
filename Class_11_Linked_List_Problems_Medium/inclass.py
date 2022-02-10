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
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev

    def deleteNode(self, key):
        current = self.head
        if self.head.data == key:
            temp_next = current.next
            current = None
            self.head = temp_next
            return
        
        prev = None

        while current.data is not None:
            prev = current
            current = current.next
            temp_next = current.next
            if current.data == key:
                break
            
        prev.next = temp_next
        current = None

    def removeDupl(self):
        current = self.head
        try:
            temp_next = current.next
        except:
            return
        
        while temp_next:
            if temp_next.data == current.data:
                current.next = temp_next.next
            else:
                current = current.next
            temp_next = current.next

    def removeDuplUnsorted(self):
        dupSet = {}
        
        current = self.head
        prev = None

        while current:
            if current.data in dupSet.keys():
                prev.next = current.next
            else:
                dupSet[current.data] = True
                prev = current
                
            current = current.next
            
    def deleteSpecific(self, m, n):
        current = self.head
        prev = None
        for i in range(1, m):
            try:
                prev = current
                current = current.next
            except:
                return
                
        while n > 0:
            try:
                prev.next = current.next
                current = prev.next
            except:
                return
            n -= 1


                

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.insert(7)
LL.insert(7)
LL.insert(7)
LL.insert(5)


LL.printLL()

print()

LL.reverseLL()
LL.printLL()

print()

LL.deleteNode(5)
LL.printLL()



print()
LL.removeDuplUnsorted()
LL.printLL()

print()
LL.deleteSpecific(3,2)
LL.printLL()