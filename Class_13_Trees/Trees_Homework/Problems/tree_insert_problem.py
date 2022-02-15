# Write code for a node and an insert function to create a binary tree

# creating the node class for the tree
class Node:
    # constructor
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
# function for inserting node into tree
def insertNode(root, key):
    
    #if the tree is empty, start it with the first node
    if root is None:
        return Node(key)
    else:
        #check if value is duplicate
        if root.val == key:
            return root
        #if the current node value is less than the key, move on to the right child node
        elif root.val < key:
            root.right = insertNode(root.right, key)
        #otherwise, move on to the right child node
        else:
            root.left = insertNode(root.left, key)
        
    return root

#function for printing tree in order
def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print(root.val)
        inorderPrint(root.right)

#function for searching binary tree
def searchNodes(root, key):
    #check base case that root is empty or has the right value
    if root is None or root.val == key:
        return root
    
    #check comparison of key to root.value
    if root.val < key:
        return searchNodes(root.right, key)
    else:
        return searchNodes(root.left, key)

root = Node(50)
insertNode(root, 30)
insertNode(root, 20)
insertNode(root, 40)
insertNode(root, 70)
insertNode(root, 60)
insertNode(root, 80)

print(root)

print()

inorderPrint(root)
