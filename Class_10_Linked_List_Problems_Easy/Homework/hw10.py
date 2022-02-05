# create node class
class Node:

    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:

    #constructor
    def __init__(self):
        self.head = None

    #output list function
    def printList(self):
        outputString = ''
        temp = self.head
        #check if there's a node linked to the previous node
        while (temp):
            outputString += str(temp.data)
            temp = temp.next

        return outputString

#empty list
lList = LinkedList()

#create 3 nodes, first is already in linkedlist
lList.head = Node(1)
second = Node(2)
third = Node(3)

#link list to second node
lList.head.next = second

#link second node in list to third node
second.next = third

#test function for returning the values in a linnkedList
print(lList.printList())