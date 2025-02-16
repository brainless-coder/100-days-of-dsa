import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelWiseInput():
    tree = [int(x) for x in input().split()]
    rootData = tree.pop(0)
    if rootData == -1:
        return
    root = BinaryTreeNode(rootData)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currNode = q.get()
        leftChild = tree.pop(0)
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currNode.left = leftNode
            q.put(currNode.left)

        rightChild = tree.pop(0)
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currNode.right = rightNode
            q.put(currNode.right)
    return root

def printLevelWise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currNode = q.get()
        if currNode != None:
            print(currNode.data, end=" ")
            q.put(currNode.left)
            q.put(currNode.right)


def searchBST(root, k):
    if root is None:
        return False
    if root.data == k:
        return True
    elif k < root.data:
        return searchBST(root.left, k)
    else:
        return searchBST(root.right, k)

def eleBetK1K2(root, k1, k2):
    if root is None:
        return
    if root.data < k1:
        eleBetK1K2(root.right, k1, k2)
    elif root.data > k2:
        eleBetK1K2(root.left, k1, k2)
    else:
        eleBetK1K2(root.left, k1, k2)
        print(root.data, end=" ")
        eleBetK1K2(root.right, k1, k2)
    
def sortedArrayToBST(arr):
    if len(arr) == 0:
        return
    mid = len(arr)//2
    root = BinaryTreeNode(arr[mid])
    left = sortedArrayToBST(arr[:mid])
    right = sortedArrayToBST(arr[mid+1:])
    root.left = left
    root.right = right
    return root

def minTree(root):
    if root is None:
        return 99999
    left = minTree(root.left)
    right = minTree(root.right)
    return min(left, right, root.data)

def maxTree(root):
    if root is None:
        return -1
    left = maxTree(root.left)
    right = maxTree(root.right)
    return max(left, right, root.data)

def isBST(root):
    if root is None:
        return True
    if maxTree(root.left) < root.data and minTree(root.right) >= root.data:
        return isBST(root.left) and isBST(root.right)
    else:
        return False
    
def isBST2(root, maxmin = ""):
    if root is None:
        if maxmin == "max":
            return (-1, True)
        else:
            return (999, True)
    
    leftMax, isLeftBST = isBST2(root.left, "max")
    rightMin, isRightBST = isBST2(root.right, "min")
    if leftMax < root.data and rightMin >= root.data:
        if isLeftBST and isRightBST:
            if leftMax == -1 and rightMin == 999:
                return root.data, True
            if maxmin == "max":
                if rightMin == 999:
                    return max(leftMax, root.data), True
                return max(leftMax, rightMin, root.data), True
            else:
                if leftMax == -1:
                    return min(rightMin, root.data), True
                return min(leftMax, rightMin, root.data), True
    return 999, False

def isBST3(root, minRange = -1000, maxRange = 1000):
    if root is None:
        return True
    if root.data > minRange and root.data <= maxRange:
        return isBST3(root.left, minRange, root.data-1) and isBST3(root.right, root.data, maxRange)
    return False

def isBST4(root):
    if root is None:
        return 999, -999, True
    leftMin, leftMax, leftBST = isBST4(root.left)
    rightMin, rightMax, rightBST = isBST4(root.right)
    minm = min(leftMin, rightMin, root.data)
    maxm = max(leftMax, rightMax, root.data)
    isTreeBST = False
    if root.data > leftMax and root.data <= rightMin:
        isTreeBST = leftBST and rightBST
    return minm, maxm, isTreeBST


root = levelWiseInput()
# k = input().split()
# k1 = int(k[0])
# k2 = int(k[1])
# print(searchBST(root, k))
# eleBetK1K2(root, k1, k2)
# arr = [int(x) for x in input().split()]
# root = sortedArrayToBST(arr)
# printLevelWise(root)
# print(minTree(root))
# print(maxTree(root))
print(isBST(root))
print(isBST2(root))
# print(isBST2(root)[1])
print(isBST3(root))
print(isBST4(root))