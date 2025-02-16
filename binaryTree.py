import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def printTree(root):
    if root is None:
        return
    print(root.data, end=": ")
    if root.left is not None and root.right is not None:
        print("L", root.left.data, end=", ")
    elif root.left is not None:
        print("L", root.left.data, end="")
    if root.right is not None:
        print("R", root.right.data, end="")
    print()
    printTree(root.left)
    printTree(root.right)

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def numNodes(root):
    if root is None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return leftCount + rightCount + 1

def sumOfNodes(root):
    if root is None:
        return 0
    leftSum = sumOfNodes(root.left)
    rightSum = sumOfNodes(root.right)
    return root.data + leftSum + rightSum

def printPreOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    printPreOrder(root.left)
    printPreOrder(root.right)

def printPostOrder(root):
    if root is None:
        return
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.data, end=" ")

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)

def largestData(root):
    if root is None:
        return -1
    data = root.data
    leftData = largestData(root.left)
    rightData = largestData(root.right)
    return max(data, leftData, rightData)

def nodesGreaterThanX(root, x):
    if root is None:
        return 0
    count = 0
    if root.data > x:
        count += 1
    leftCount = nodesGreaterThanX(root.left, x)
    rightCount = nodesGreaterThanX(root.right, x)
    return count + leftCount + rightCount

def heightOfTree(root):
    if root is None:
        return 0
    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    return 1 + max(leftHeight, rightHeight)

def numLeafNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    return numLeafLeft + numLeafRight

def printNodesAtDepthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")
        return
    printNodesAtDepthK(root.left, k-1)
    printNodesAtDepthK(root.right, k-1)

def printNodesAtDepthK2(root, k, d = 0):
    if root is None:
        return
    if k == d:
        print(root.data, end=" ")
    printNodesAtDepthK2(root.left, k, d+1)
    printNodesAtDepthK2(root.right, k, d+1)

def replaceNodeWithDepth(root, d = 0):
    if root is None:
        return
    root.data = d
    replaceNodeWithDepth(root.left, d+1)
    replaceNodeWithDepth(root.right, d+1)

def isNodePresent(root, X):
    if root is None:
        return False
    if root.data == X:
        return True
    ans = isNodePresent(root.left, X)
    if ans:
        return ans
    return isNodePresent(root.right, X)

def nodesWithoutSibling(root):
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data, end=" ")
    if root.left is None and root.right is not None:
        print(root.right.data, end=" ")
    nodesWithoutSibling(root.left)
    nodesWithoutSibling(root.right)

def removeLeafNodes(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = removeLeafNodes(root.left)
    root.right = removeLeafNodes(root.right)
    return root

def mirrorBinaryTree(root):
    if root is None:
        return None
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    root.left, root.right = root.right, root.left

def isBalanced(root):
    if root is None:
        return True
    lh = heightOfTree(root.left)
    rh = heightOfTree(root.right)
    if lh-rh > 1 or rh-lh > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    return False

def isBalancedOpti(root):
    if root is None:
        return 0, True
    lh, isLeftBalanced = isBalancedOpti(root.left)
    rh, isRightBalanced = isBalancedOpti(root.right)
    h = 1 + max(lh, rh)
    if lh-rh > 1 or rh-lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    return h, False

# agar main fn se bas balanced waala part return karna h to
def isBalanced2(root):
   h, ans =  isBalancedOpti(root)
   return ans

def diameter(root):
    if root is None:
        return 0
    lh = heightOfTree(root.left)
    rh = heightOfTree(root.right)
    ld = diameter(root.left)
    rd = diameter(root.right)
    return max((lh+rh), ld, rd)

def diameterOpti(root):
    if root is None:
        return 0, 0
    lh, ld = diameterOpti(root.left)
    rh, rd = diameterOpti(root.right)
    h = 1+max(lh, rh)
    return h, max(lh+rh, ld, rd)

def levelWiseInput():
    q = queue.Queue()
    rootData = int(input("Enter Root node: "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input(f"Enter left child of {currentNode.data}: "))
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = int(input(f"Enter right child of {currentNode.data}: "))
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

def printLevelWise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currNode = q.get()
        print(currNode.data, end=" ")
        if currNode.left is not None:
            q.put(currNode.left)
        if currNode.right is not None:
            q.put(currNode.right)

def printLevelWiseDetailed(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currNode = q.get()
        print(currNode.data, end=": ")
        if currNode.left is not None:
            if currNode.right is not None:
                print("L", currNode.left.data, end=", ")
            else:
                print("L", currNode.left.data, end="")
            q.put(currNode.left)
        if currNode.right is not None:
            print("R", currNode.right.data, end="")
            q.put(currNode.right)
        print()

def treeFromPreIn(preorder, inorder):
    if len(preorder) == 0:
        return None
    root = BinaryTreeNode(preorder[0])
    for i in range(0, len(inorder)):
        if inorder[i] == preorder[0]:
            rootIdxInorder = i
            break
    leftInorder = inorder[:rootIdxInorder]
    rightInorder = inorder[rootIdxInorder+1:]
    leftSize = len(leftInorder)
    leftPreorder = preorder[1:leftSize+1]
    rightPreorder = preorder[leftSize+1:]
    root.left = treeFromPreIn(leftPreorder, leftInorder)
    root.right = treeFromPreIn(rightPreorder, rightInorder)
    return root

def treeFromPostIn(postOrder, inOrder):
    if len(postOrder) == 0:
        return None
    root = BinaryTreeNode(postOrder[-1])
    for i in range(0, len(inOrder)):
        if inOrder[i] == postOrder[-1]:
            rootIdxInorder = i
            break
    leftInorder = inOrder[0:rootIdxInorder]
    rightInOrder = inOrder[rootIdxInorder+1:]
    leftSize = len(leftInorder)
    leftPostOrder = postOrder[0:leftSize]
    rightPostOrder = postOrder[leftSize:-1]
    root.left = treeFromPostIn(leftPostOrder, leftInorder)
    root.right = treeFromPostIn(rightPostOrder, rightInOrder)
    return root

def createInsertDupNode(root):
    if root is None:
        return None
    createInsertDupNode(root.left)
    createInsertDupNode(root.right)
    newNode = BinaryTreeNode(root.data)
    newNode.left = root.left
    root.left = newNode

def minMaxOfTree(root):
    if root is None:
        return (9999, -1)
    minL, maxL = minMaxOfTree(root.left)
    minR, maxR = minMaxOfTree(root.right)
    minm = minL if minL < minR else minR
    maxm = maxL if maxL > maxR else maxR
    if root.data < minm:
        minm = root.data
    if root.data > maxm:
        maxm = root.data
    return (minm, maxm)
    
def levelOrderTraversal(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    q.put(None)

    while not q.empty():
        currNode = q.get()
        if currNode is None:
            if not q.empty():
                print()
                q.put(None)
        else:
            print(currNode.data, end=" ")
            if currNode.left != None:
                q.put(currNode.left)
            if currNode.right is not None:
                q.put(currNode.right)

def pathSumRootToLeaf(root, k, s=""):
    if root is None:
        return
    s += f"{root.data} "
    if k == root.data and root.left is None and root.right is None:
        print(s)
    pathSumRootToLeaf(root.left, k-root.data, s)
    pathSumRootToLeaf(root.right, k-root.data, s)

def printNodesAtDistKFromNode(root, targetNode, k, path = []):
    if root is None:
       return
    if root.data == targetNode:
        printNodesAtDepthK(root, k)
        path.reverse()
        for i in range(len(path)):
            if path[i][1] == 'L':
                printNodesAtDepthK(path[i][0].right, k-i-2)
            else:
                printNodesAtDepthK(path[i][0].left, k-i-2)
        return
    path.append((root, 'L'))
    printNodesAtDistKFromNode(root.left, targetNode, k, path)
    path.pop()
    path.append((root, 'R'))
    printNodesAtDistKFromNode(root.right, targetNode, k, path)
    path.pop()

def nodeToRootPath(root, k, path = []):
    if root is None:
        return
    if root.data == k:
        path.append(root.data)
        path.reverse()
        print(path)
    path.append(root.data)
    nodeToRootPath(root.left, k, path)
    nodeToRootPath(root.right, k, path)
    path.pop()


def rootToNodePath2(root, k):
    if root is None:
        return None
    if root.data == k:
        li = []
        li.append(root.data)
        return li
    leftOutput = rootToNodePath2(root.left, k)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = rootToNodePath2(root.right, k)
    if rightOutput is not None:
        rightOutput.append(root.data)
        return rightOutput
    return None




# btn1 = BinaryTreeNode(1)
# btn2 = BinaryTreeNode(4)
# btn3 = BinaryTreeNode(5)
# btn4 = BinaryTreeNode(12)
# btn5 = BinaryTreeNode(15)
# btn1.left = btn2
# btn1.right = btn3
# btn2.left = btn4
# btn3.left = btn5

# printTree(btn1)
# printTree(None)

root = treeInput()
# root = levelWiseInput()
printLevelWiseDetailed(root)
# printTree(root)
# print(numNodes(root))
# print(sumOfNodes(root))
# printPreOrder(root)
# printPostOrder(root)
# printInOrder(root)
# print(largestData(root))
# x = int(input())
# print(nodesGreaterThanX(root, x))
# print(heightOfTree(root))
# print(numLeafNodes(root))
# printNodesAtDepthK(root, 2)
# printNodesAtDepthK2(root, 2)
# replaceNodeWithDepth(root)
# printTree(root)
# print(isNodePresent(root, x))
# nodesWithoutSibling(root)
# root = removeLeafNodes(root)
# mirrorBinaryTree(root)
# printTree(root)
# print(isBalanced(root))
# print(isBalancedOpti(root))
# print(isBalanced2(root))
# print(diameter(root))
# print(diameterOpti(root))
# printLevelWise(root)
# preOrder = [int(x) for x in input().split()]
# postOrder = [int(x) for x in input().split()]
# inOrder = [int(x) for x in input().split()]
# root = treeFromPreIn(preOrder, inOrder)
# root = treeFromPostIn(postOrder, inOrder)
# createInsertDupNode(root)
# printLevelWiseDetailed(root)
# print(minMaxOfTree(root))
# levelOrderTraversal(root)
# pathSumRootToLeaf(root, k)
# targetNode = int(input())
k = int(input())
# printNodesAtDistKFromNode(root, targetNode, k)
nodeToRootPath(root, k)
print()
print(rootToNodePath2(root, k))