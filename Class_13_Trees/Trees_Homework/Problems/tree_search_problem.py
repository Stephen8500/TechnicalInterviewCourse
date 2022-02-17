# Write code for a search function for a binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, val):
        if self.val == None:
            self.val = val
            return
        
        if self.val == val:
            return
        elif self.val < val:
            if self.right:
                self.right.insert(val)
                return
            self.right = Node(val)
        else:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)

    def printTree(self):
        if self.val:
            if self.left:
                self.left.printTree()
            print(self.val)
            if self.right:
                self.right.printTree()
    
    def searchTree(self, val):
        if self.val:
            if self.val == val:
                return True
            elif self.val < val:
                if self.right:
                    return self.right.searchTree(val)
            else:
                if self.left:
                    return self.left.searchTree(val)
        return False

    def searchLevel(self, val, level = 1):
        if self.val:
            if self.val == val:
                return level
            elif self.val < val:
                if self.right:
                    level += 1
                    return self.right.searchLevel(val, level)
            else:
                if self.left:
                    level += 1
                    return self.right.searchLevel(val, level)
        return False

root = Node(9)
root.insert(3)
root.insert(24)
root.insert(20)
root.insert(5)
root.insert(2)
root.insert(40)
root.insert(35)

root.printTree()

print()

print(root.searchTree(20))

print(root.searchTree(45))

print(root.searchLevel(40))