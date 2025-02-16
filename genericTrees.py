import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):
    # here None is not a base case but an edge case
    # bcoz agar root ke childrens None hai to wo case apan niche loop me handle kar rhe hai
    if root is None:
        return
    print(root.data)
    # agar root ke childrens nhi honge to hum loop me ghusenge hi nhi
    # here leaf node is the base case kyunki hum iss chij ko dekh rhe h
    # jo agar root ke children nhi h, matlab leaf node h
    # then hum aage ke recursive calls nhi kar rhe h
    # so, here effectively, leaf node is the base case
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=": ")
    for ele in root.children:
        print(ele.data, end=", ")
    print()
    for child in root.children:
        printTreeDetailed(child)

def treeInput():
    rootData = int(input("Enter root data: "))
    # Not a base case but an edge case
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    noOfChild = int(input(f"Enter no of childrens for {rootData}: "))
    for i in range(noOfChild):
        child = treeInput()
        root.children.append(child)
    return root

def noOfNodes(root):
    # not a base case, but an edge case
    if root is None:
        return 0
    count = 1
    for child in root.children:
        count += noOfNodes(child)
    return count

def sumOfNodes(root):
    # not a base case, but an edge case
    if root is None:
        return 0
    sum = root.data
    for child in root.children:
        sum += sumOfNodes(child)
    return sum

def treeInputLevelWise():
    rootData = int(input("Enter root data: "))
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        childCount = int(input(f"Enter no of children of {currentNode.data}: "))
        for i in range(childCount):
            childNodeData = int(input(f"Enter next child of {currentNode.data}: "))
            childNode = TreeNode(childNodeData)
            currentNode.children.append(childNode) 
            q.put(childNode)
    return root

def nodeWithLargestData(root):
    if root is None:
        return None
    maxm = root.data
    for child in root.children:
        childMax = nodeWithLargestData(child)
        maxm = max(maxm, childMax)
    return maxm

def heightOfTree(root):
    if root is None:
        return None
    li = []
    for child in root.children:
        childHeight = heightOfTree(child)
        li.append(childHeight)
    if len(li) == 0:
        return 1
    height = max(li) + 1
    return height

def printTreeLevelWise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        print(currentNode.data, end=": ")
        for child in currentNode.children:
            print(child.data, end=", ")
            q.put(child)
        print()


# n1 = TreeNode(5)
# n2 = TreeNode(2)
# n3 = TreeNode(9)
# n4 = TreeNode(8)
# n5 = TreeNode(7)
# n6 = TreeNode(15)
# n7 = TreeNode(1)
# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)
# n3.children.append(n6)
# n3.children.append(n7)

# printTree(n1)
# printTree(None)
# printTreeDetailed(n1)
# printTreeDetailed(None)
# root = treeInput()
root = treeInputLevelWise()
# printTreeDetailed(root)
printTreeLevelWise(root)
print("No of Nodes in Tree:", noOfNodes(root))
print("Sum of Nodes in Tree:", sumOfNodes(root))
print("Maximum Node in Tree:", nodeWithLargestData(root))
print("Height of Tree:", heightOfTree(root))