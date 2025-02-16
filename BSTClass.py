class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def isPresentHelper(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.isPresentHelper(root.left, data)
        return self.isPresentHelper(root.right, data)

    def isPresent(self, data):
        return self.isPresentHelper(self.root, data)

    def printTreeHelper(self, root):
        if root is None:
            return
        print(root.data, end=": ")
        if root.left is not None:
            print('L', root.left.data, end=", ")
        if root.right is not None:
            print('R', root.right.data, end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def insertHelper(self, root, data):
        if root is None:
            node = BinaryTreeNode(data)
            return node
        if data < root.data:
            root.left = self.insertHelper(root.left, data)
            return root
        root.right = self.insertHelper(root.right, data)
        return root
        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)

    def deleteHelper(self, root, data):
        pass
            
    def min(self, root):
        pass

    def delete(self, data):
        pass

    def count(self):
        return self.numNodes


b = BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree()
print(b.count())
print(b.delete(10))
b.printTree()
print(b.count())