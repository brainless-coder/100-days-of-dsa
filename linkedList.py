class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def takeInput():
    inputList = [int(x) for x in input().split()]
    head = tail = None

    for currEle in inputList:
        if currEle == -1:
            break

        newNode = Node(currEle)
        if head is None:
            head = tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
    return head

def printLL(head):
    while head is not None:
        print(head.data, end='-> ')
        head = head.next
    print(None)
    return

def lengthLL(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length

def printIthNode(head, index):
    i = 0
    while head is not None:
        if index == i:
            print(head.data)
            return
        i += 1
        head = head.next

def insertAtIth(head, i, data):
    size = lengthLL(head)
    if i > size or i < 0:
        print("Invalid index, greater or smaller than size of LL")
        return head

    count = 0
    newNode = Node(data)
    curr = head
    while count < i-1:
        curr = curr.next
        count += 1

    if i == 0:
        newNode.next = curr
        head = newNode
    else:
        newNode.next = curr.next
        curr.next = newNode
    return head

def deleteNode(head, pos):
    size = lengthLL(head)
    if pos < 0 or pos > size:
        print("Invalid Index, greater or smaller than size of LL")
        return head
    i = 0
    curr = head
    prev = None

    while i < pos:
        prev = curr
        curr = curr.next
        i += 1
    if prev is None:
        head = curr.next
    else:
        prev.next = curr.next
    del curr
    return head

def lengthLLRecur(head):
    if head.next is None:
        return 1
    return lengthLLRecur(head.next) + 1

# O(i) if the length is correct
def insertAtIthRecur(head, i , data):
    if i < 0:
        return head
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead = insertAtIthRecur(head.next, i-1, data)
    head.next = smallHead
    return head

def deleteNodeRecur(head, i):
    if i < 0:
        return head
    if i == 0:
        curr = head
        head = curr.next
        del curr
        return head
    if head is None:
        return None
    smallHead = deleteNodeRecur(head.next, i-1)
    head.next = smallHead
    return head

def applendLastNToFirst(head, n):
    if n == 0:
        return head
    length = lengthLL(head)
    i = 1
    curr = tail = head
    
    while i < length-n:
        curr = curr.next
        i += 1

    h2 = curr.next
    curr.next = None
    curr = h2

    while curr is not None:
        if curr.next is None:
            tail = curr
        curr = curr.next

    tail.next = head
    head = h2
    return head

def eliminateConsDup(head):
    curr = head

    while curr is not None:
        if curr.next is not None and curr.data == curr.next.data:
            temp = curr.next
            curr.next = temp.next
            temp.next = None
            del temp

        if curr.next is None or curr.data != curr.next.data:
            curr = curr.next

def printReverseLL(head):
    if head.next is None:
        print(head.data, end=" ")
        return
    printReverseLL(head.next)
    print(head.data, end=" ")

def palindrome(head):
    li1 = []
    while head is not None:
        li1.append(head.data)
        head = head.next
    li2 = li1[::-1]
    if li1 == li2:
        return True
    return False

def reverseLL1(head):
    if head is None or head.next is None:
        return head
    smallHead = reverseLL1(head.next)
    tail = smallHead
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    head.next = None
    return smallHead

def reverseLL2(head):
    if head is None or head.next is None:
        return head, head
    sh, st = reverseLL2(head.next)
    st.next = head
    head.next = None
    return sh, head

def reverseLL3(head):
    if head is None or head.next is None:
        return head
    smallHead = reverseLL3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

def reverseLL4(head):
    if head is None:
        return head
    prev = None
    curr = head
    temp = curr.next

    while temp is not None:
        curr.next = prev
        prev = curr
        curr = temp
        temp = temp.next
    curr.next = prev
    return curr

# Here we need 2 passes of LL
def midLLNaive(head):
    n = lengthLL(head)
    if n == 0:
        return head
    if n%2 == 0:
        mid = n//2 - 1
    else:
        mid = n//2
    i = 0
    curr = head
    while i < mid:
        curr = curr.next
        i += 1
    return curr.data
    
# In Single pass of LL
def midLLOptimized(head):
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next 
    return slow.data 

def merge(h1, h2):
    finalHead = finalTail = None

    while h1 is not None and h2 is not None:
        if h1.data <= h2.data:
            if finalHead is None:
                finalHead = finalTail = h1
            else:
                finalTail.next = h1
                finalTail = finalTail.next
            h1 = h1.next
        else:
            if finalHead is None:
                finalHead = finalTail = h2
            else:
                finalTail.next = h2
                finalTail = finalTail.next
            h2 = h2.next

    while h1 is not None:
        finalTail.next = h1
        finalTail = finalTail.next
        h1 = h1.next

    while h2 is not None:
        finalTail.next = h2
        finalTail = finalTail.next
        h2 = h2.next

    return finalHead

def mergeSort(head):
    if head is None or head.next == None:
        return head
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    head2 = slow.next
    slow.next = None
    head = mergeSort(head)
    head2 = mergeSort(head2)
    head = merge(head, head2)
    return head

def findNodeRecur(head, i, x):
    if head is None:
        return -1
    if head.next is None:
        if head.data == x:
            return i
        else:
            return -1
    if head.data == x:
        return i
    ans = findNodeRecur(head.next, i, x)
    if ans == -1:
        return -1
    return ans+1

def evenAfterOddEle(head):
    evenHead = evenTail = oddHead = oddTail = None
    while head is not None:
        if head.data%2 == 0:
            if evenHead is None:
                evenHead = evenTail = head
            else:
                evenTail.next = head
                evenTail = evenTail.next
        else:
            if oddHead is None:
                oddHead = oddTail = head
            else:
                oddTail.next = head
                oddTail = oddTail.next
        head = head.next

    if evenHead is None:
        return oddHead
    if oddHead is None:
        return evenHead

    oddTail.next = evenHead
    evenTail.next = None
    return oddHead

def delNnodeafterMnode(head, m, n):
    if m == 0:
        head = None
    curr = head
    while curr is not None:
        i = 1
        while i < m:
            i += 1
            curr = curr.next
        temp = curr.next
        j = 0
        while j < n and temp is not None:
            j += 1
            temp = temp.next
        curr.next = temp
        if curr is not None:
            curr = curr.next
    return head

# swaps two nodes at positions i and j, without swapping the values
def swapTwoNodes(head, i , j):
    n = lengthLL(head)
    if i == j:
        return head
    if i > j:
        i, j = j, i
    it = 0
    p1 = head
    if i == 0:
        c1 = head
        c1next = head.next
    else:
        while it < i-1:
            p1 = p1.next
            it += 1
        c1 = p1.next
    
    it = 0
    p2 = head
    while it < j-1:
        p2 = p2.next
        it += 1
    c2 = p2.next

    if i == 0:
        if j == 1:
            c1.next = c2.next
            c2.next = c1
        else:
            p2.next = c1
            c1.next = c2.next
            c2.next = c1next
        head = c2
    else:
        p1.next = c2
        p2.next = c1
        if j == n-1:
            c2.next = c1.next
            c1.next = None
        else:
            c1.next = c2.next
            c2.next = p2
    return head

# This reverses a linked list in groups of k nodes.
def kReverse(head, k):
    if head is None:
        return
    h1 = t1 = head
    count = 1
    while count < k:
        if t1.next is None:
            break
        t1 = t1.next
        count += 1
    h2 = t1.next
    t1.next = None
    h1, t1 = reverseLL2(h1)
    h2 = kReverse(h2, k)
    t1.next = h2
    return h1

def bubbleSort(head):
    n = lengthLL(head)
    i = 0
    while i < n-1:
        prev = None
        curr = head
        while curr.next is not None:
            if curr.data > curr.next.data:
                curr = swapTwoNodes(curr, 0, 1) 
                if curr.next is head:
                    head = curr
                if curr is not head:
                    prev.next = curr

            prev = curr
            curr = curr.next
        i += 1
    return head

head = takeInput()
# head2 = takeInput()
printLL(head)
# printLL(head2)
# print(lengthLL(head))
# index = int(input())
# printIthNode(head, index)
# data = int(input())
# head = insertAtIth(head, index, data)
# head = deleteNode(head, index)
# print(lengthLLRecur(head))
# head = insertAtIthRecur(head, index, data)
# head = deleteNodeRecur(head, index)
# n = int(input())
# head = applendLastNToFirst(head, n)
# eliminateConsDup(head)
# printReverseLL(head)
# print(palindrome(head))
# head = reverseLL1(head)
# head, tail = reverseLL2(head)
# head = reverseLL3(head)
# head = reverseLL4(head)
# print(midLLNaive(head))
# print(midLLOptimized(head))
# head = merge(head1, head2)
# head = mergeSort(head)
# x = int(input())
# ans = findNodeRecur(head, 0, x)
# print(ans)
# head = evenAfterOddEle(head)
# s = input().split()
# m, n = int(s[0]), int(s[1])
# head = delNnodeafterMnode(head, m, n)
# head = swapTwoNodes(head, m, n)
# k = int(input())
# head = kReverse(head, k)
head = bubbleSort(head)
printLL(head)
