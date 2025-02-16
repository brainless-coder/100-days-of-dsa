import sys
sys.setrecursionlimit(3000)

# Fibonacci Number
def fibonacci(n):
    # 2 recursive calls so 2 base cases
    if n == 1 or n == 2:
        return 1
    fib1 = fibonacci(n-1)
    fib2 = fibonacci(n-2)
    return fib1 + fib2

n = int(input())
print(fibonacci(n))


# Check if List is sorted or not
def isSortedList(li):
    n = len(li)
    if n == 0 or n == 1:
        return True
    if li[0] > li[1]:
        return False
    return isSortedList(li[1:])

def isSortedList(li, start, n):
    if start == n-1 or start == n:
        return True
    if li[start] > li[start+1]:
        return False
    return isSortedList(li, start+1, n)

# Sum of List
def listSum(li):
    n = len(li)
    if n == 1:
        return li[0]
    return li[0] + listSum(li[1:])
 
# li = [int(ele) for ele in input().split()]
# print(isSortedList(li))
# print(listSum(li))
# print(isSortedList(li, 0, len(li)))

# Check Number in Array
def xinArray(li, x):
    n = len(li)
    if n == 0:
        return False
    if li[0] == x:
        return True
    return xinArray(li[1:], x)

def firstIndexOfNumber(li, start, x):
    n = len(li)
    if start == n:
        return -1
    if li[start] == x:
        return start
    return firstIndexOfNumber(li, start+1, x)

def lastIndexOfNumber(li, start, x):
    if start == -1:
        return -1
    if li[start] == x:
        return start
    return lastIndexOfNumber(li, start-1, x)

def lastIndexOfNumber(li, x):
    n = len(li)
    if n == 0:
        return -1
    smallerOutput = lastIndexOfNumber(li[1:], x)
    if smallerOutput == -1:
        if li[0] == x:
            return 0
        else:
            return -1
    else:
        return smallerOutput+1

# li = [int(ele) for ele in input().split()]
# x = int(input())
# print(xinArray(li, x))
# print(firstIndexOfNumber(li, 0, x))
# print(lastIndexOfNumber(li, len(li)-1, x))
# print(lastIndexOfNumber(li, x))


# Replace occurences of a character
def replaceChar(s, a, b):
    ans = ''
    if len(s) == 0:
        return s
    if s[0] == a:
        ans += b
    else:
        ans += s[0]
    return ans + replaceChar(s[1:], a, b)
    
# Remove x from string
def removex(s):
    if len(s) == 0:
        return s
    if s[0] == 'x':
        return removex(s[1:])
    else:
        return s[0] + removex(s[1:])

# Replace pi with 3.14 in string
def replacePi(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == 'p' and s[1] == 'i':
        return '3.14' + replacePi(s[2:])
    else:
        return s[0] + replacePi(s[1:])

# Remove Consecutive Dupliates from a string
def removeConsDup(s):
    n = len(s)
    i, j = 0, 1
    newStr = ""
    while j < n:
        if s[i] != s[j]:
            newStr += s[i]
           
        i += 1
        j += 1
    newStr += s[i]
    
    return newStr


# Remove Consecutive Dupliates from a string recursively
def removeConsDupRec(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] != s[1]:
        return s[0] + removeConsDupRec(s[1:])
    return removeConsDupRec(s[1:])



# s = input()
# print(replaceChar(s, 'l', 'x'))
# print(removex(s))
# print(replacePi(s))
# print(removeConsDup(s))
# print(removeConsDupRec(s))


# Binary Search Recursively
def binarySearch(li, s, e, x):
    mid = (s+e)//2
    if s > e:
        return -1
    if li[mid] == x:
        return mid
    elif li[mid] > x:
        return binarySearch(li, s, mid-1, x)
    else:
        return binarySearch(li, mid+1, e, x)

# li = [1, 3, 4, 6, 7, 8, 9, 10, 12, 15]
# x = int(input())
# print(binarySearch(li, 0, len(li)-1, x))


# Merge Sort
def mergeSort(li):
    if len(li) == 0 or len(li) == 1:
        return
    mid = len(li)//2
    s1, s2 = li[:mid], li[mid:]
    mergeSort(s1)
    mergeSort(s2)
    merge(s1, s2, li)

def merge(l1, l2, li):
    n, m = len(l1), len(l2)
    i, j, k = 0, 0, 0

    while (i < n and j < m):
        if l1[i] <= l2[j]:
            li[k] = l1[i]
            i += 1
        else:
            li[k] = l2[j]
            j += 1
        k += 1
    
    while i < n:
        li[k] = l1[i]
        i += 1
        k += 1
    while j < m:
        li[k] = l2[j]
        j += 1
        k += 1


# Quick Sort
def quickSort(li, s, e):
    if s >= e:
        return
    pivotIdx = partition(li, s, e)
    quickSort(li, s, pivotIdx-1)
    quickSort(li, pivotIdx+1, e)

def partition(li, s, e):
    pivot = s
    for i in range(s, e+1):
        if li[i] < li[s]:
            pivot += 1

    li[pivot], li[s] = li[s], li[pivot]

    i, j = s, e
    while i < j:
        if li[i] < li[pivot]:
            i += 1
        elif li[j] >= li[pivot]:
            j -= 1
        else:
            li[i] , li[j] = li[j], li[i]
            i += 1
            j -= 1
            
    return pivot

# li = [5, 2, 7, 9, 1, 7, 4, 3, 0, 67, 34, 12]
# mergeSort(li)
# quickSort(li, 0, len(li)-1)
# print(li)


# Tower of Hanoi
def towerOfHanoi(n, src, aux, des):
    if n == 1:
        print("move 1st disk from " + src + " to " + des)
        return
    towerOfHanoi(n-1, src, des, aux)
    print("move " + str(n) +" th disk from " + src + " to " + des)
    towerOfHanoi(n-1, aux, src, des)

# towerOfHanoi(4, 'a', 'b', 'c')


# Geometric Sum: given k, find geometric sum
# i.e.  1 + 1/2 + 1/4 + 1/8 + ..... + 1/2^k
def geometricSum(k):
    if k == 0:
        return 1
    ans = (1/(2**k) + geometricSum(k-1))
    ans = round(ans, 5)
    return ans

# k = int(input())
# print(geometricSum(k))


# palindrome String
def palindromeString(s):
    n = len(s)
    if n == 0 or n == 1:
        return True
    if s[0] != s[n-1]:
        return False
    return palindromeString(s[1:n-1])

# s = input()
# print(palindromeString(s))


# String to Integer
def stringToInt(s):
    n = len(s)
    if n == 1:
        return int(s)
    return int(s[n-1]) + stringToInt(s[:n-1])*10

# s = input()
# print(stringToInt(s))
# print(type(s))
# print(type(stringToInt(s)))


# Pair Star: Identical adjacent char should be separated by a * 
def pairStar(s):
    ans = s[0]
    n = len(s)
    if n == 1:
        return ans
    if s[0] == s[1]:
        ans += '*' 
    return ans + pairStar(s[1:])

# s = input()
# print(pairStar(s))


# Check AB
def checkAB(s, start):
    n = len(s)
    if s[0] != 'a':
        return False
    if start == n-1:
        return True
    if s[start] == 'a':
        if s[start+1] == 'a':
            return checkAB(s, start+1)
        elif s[start+1] == 'b':
            if start == n-2:
                return False
            if s[start+2] == 'b':
                return checkAB(s, start+1)
        else:
            return False
    
    if s[start] == 'b' and s[start+1] != 'b':
        return False

    if s[start] == 'b' and s[start+1] == 'b':
        if start == n-2:
            return True
        elif s[start+2] == 'a':
            return checkAB(s, start+2)
        else:
            return False
    else:
        return False

# s = input()
# print(checkAB(s, 0))


# Staircase: no of ways to climb stair with 1, 2, 3 steps
def staircase(n):
    # 3 Recursive calls, so 3 base cases
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    x = staircase(n-1)
    y = staircase(n-2)
    z = staircase(n-3)
    return x+y+z

# n = int(input())
# print(staircase(n))


# Power of a number: x^n in O(logn) T.C.
def power(x, n):
    if n == 0:
        return 1
    smallPow = power(x, n//2)
    if n%2 == 0:
        return smallPow*smallPow
    else:
        return x*smallPow*smallPow

# s = input().split()
# x, n = int(s[0]), int(s[1])
# print(power(x, n))


# Equilibrium Index
def equiIndex(li):
    leftSum = 0
    totalSum = sum(li)
    for i in range(len(li)):
        rightSum = totalSum - leftSum - li[i]
        if leftSum == rightSum:
            return i
        else:
            leftSum += li[i]
    return -1

# li = [int(x) for x in input().split()]
# print(equiIndex(li))


# Find the Unique element in the array
def uniqueEle(arr):
    arr.sort()
    i = 0
    while i < len(arr):
        if i == len(arr)-1:
            return arr[i]
        if arr[i] == arr[i+1]:
            i += 2
        else:
            return arr[i]


# Find Duplicate in Array: ele will be from 0 to n-2
# eg: if n = 5, ele will be from 0 to 3 in the array
def dupInArray(arr):
    n = len(arr)
    total = sum(arr)
    realSum = (n-2)*(n-1)//2
    return total - realSum

# li = [int(x) for x in input().split()]
# print(uniqueEle(li))
# print(dupInArray(li))


# Pair Sum in Array: return no of pairs whose sum is num
def pairSum(arr, num):
    pairs = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                pairs += 1
                print(arr[i], arr[j])
    return pairs

def pairSumImp(arr, num):
    pairs = 0
    freq = {}
    for ele in arr:
        if freq.get(ele) != None:
            freq[ele] += 1
        else:
            freq[ele] = 1
    for i in range(len(arr)):
        pairs += freq.get(num-arr[i], 0)
        if num-arr[i] == arr[i]:
            pairs -= 1
    return pairs//2
        

# li = [int(x) for x in input().split()]
# num = int(input())
# print(pairSum(li, num))
# print(pairSumImp(li, num))


# Rotate Array
def rotateArrayNaive1(arr, d):
    for i in range(d):
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = temp

def rotateArrayNaive2(arr, d):
    temp = [arr[x] for x in range(d)]
    for i in range(len(arr)-d):
        arr[i] = arr[i+d]
    k = 0
    for j in range(len(arr)-d, len(arr)):
        arr[j] = temp[k]
        k += 1

def rotateLeft(arr, d):
    ans = arr[d-1::-1] + arr[:d-1:-1]
    ans = ans[::-1]
    for i in range(len(ans)):
        arr[i] = ans[i]

# arr = [int(x) for x in input().split()]
# d = int(input())
# rotateArrayNaive1(arr, d)
# rotateArrayNaive2(arr, d)
# rotateLeft(arr, d)
# print(arr)


# Triplet Sum
def tripletSum(arr, num):
    pass

# li = [int(x) for x in input().split()]
# num = int(input())
# print(tripletSum(li, num))