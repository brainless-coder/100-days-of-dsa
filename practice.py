

def selectionSort(arr):
  n = len(arr)

  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    if i != min_idx:
      arr[i], arr[min_idx] = arr[min_idx], arr[i]

# arr = [int(x) for x in input().split()]
# selectionSort(arr)
# print(arr)


def bubbleSort(arr):
  n = len(arr)

  for i in range(n):
    swapped = False
    for j in range(n-1-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if (swapped == False):
      break

# arr = [int(x) for x in input().split()]
# bubbleSort(arr)
# print(arr)


def insertionSort(arr):
  n = len(arr)

  for i in range(1, n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key


# arr = [int(x) for x in input().split()]
# bubbleSort(arr)
# print(arr)


def rotateArray(arr, d):
  n, j = len(arr), 0
  temp = []

  for i in range(d):
    temp.append(arr[i])
  for i in range(n):
    if i < n-d:
      arr[i] = arr[i+d]
    else:
      arr[i] = temp[j]
      j += 1

def rotateArray2(arr, d):
  n = len(arr)
  arr[:] = arr[::-1]
  arr[:n-d] = arr[n-d-1::-1]
  arr[n-d:] = arr[n-1:n-d-1:-1]


# arr = [int(x) for x in input().split()]
# d = int(input())
# rotateArray(arr, d)
# # rotateArray2(arr, d)
# print(arr)


def checkPermutation(str1, str2):
  if len(str1) != len(str2):
    return False
  sum1 = 0
  for char in str1:
    sum1 += ord(char)
  for char in str2:
    sum1 -= ord(char)
  if sum1 != 0:
    return False
  return True

# str1 = input()
# str2 = input()
# print(checkPermutation(str1, str2))

def removeConsDup(s):
  ans = ""
  start, end = 0, len(s)

  while start < end:
    uniqueChar = s[start]
    ans += s[start]

    while start < end and s[start] == uniqueChar:
      start += 1
  
  return ans

# s = input()
# print(removeConsDup(s))

def compressString(s):
  start, end = 0, len(s)
  ans = ""

  while start < end:
    uniqueChar, count = s[start], 0

    while start < end and s[start] == uniqueChar:
      count += 1
      start += 1
    ans += uniqueChar
    if count > 1:
      ans += str(count)
  return ans

def compressString2(s):
  n = len(s)
  ans = ""
  count = 1

  for i in range(1, n):
    if s[i] == s[i-1]:
      count += 1
    else:
      if count > 1:
        ans += (s[i-1] + str(count))
      else:
        ans += s[i-1]
      count = 1
  if count > 1:
    ans += (s[n-1] + str(count))
  else:
    ans += s[n-1]
  return ans

# s = input()
# print(compressString(s))
# print(compressString2(s))

def largestRowCol(arr, n, m):
  rowSum, rowSumIdx, colSum, colSumIdx = 0, 0, 0, 0

  for i in range(n):
    sum = 0
    for j in range(m):
      sum += arr[i][j]
    if sum > rowSum:
      rowSum = sum
      rowSumIdx = i
  
  for i in range(m):
    sum = 0
    for j in range(n):
      sum += arr[j][i]
    if sum > colSum:
      colSum = sum
      colSumIdx = i
  
  if rowSum >= colSum:
    return f'row {rowSumIdx} {rowSum}'
  else:
    return f'column {colSumIdx} {colSum}'

# s = input().split()
# n, m = int(s[0]), int(s[1])
# arr = [[int(x) for x in input().split()] for i in range(n)]
# print(largestRowCol(arr, n, m))

def waveArray(arr, n, m):
  for i in range(m):
    if i%2 == 0:
      for j in range(n):
        print(arr[j][i], end=' ')
    else:
      for j in range(n-1, -1, -1):
        print(arr[j][i], end=' ')

# s = input().split()
# n, m = int(s[0]), int(s[1])
# arr = [[int(x) for x in input().split()] for i in range(n)]
# waveArray(arr, n, m)

def spiralPrint(arr, n, m):
  numEle = n*m
  count = rowStart = colStart = 0

  while count < numEle:
    i = rowStart
    while i < m and count < numEle:
      print(arr[rowStart][i], end=' ')
      i += 1
      count += 1
    rowStart += 1

    i = colStart + 1
    while i < n and count < numEle:
      print(arr[i][m-1], end=' ')
      i += 1
      count += 1
    m -= 1

    i = m-1
    while i >= colStart and count < numEle:
      print(arr[n-1][i], end=' ')
      i -= 1
      count += 1
    n -= 1

    i = n-1
    while i >= rowStart and count < numEle:
      print(arr[i][colStart], end=' ')
      i -= 1
      count += 1
    colStart += 1

# s = input().split()
# n, m = int(s[0]), int(s[1])
# arr = [[int(x) for x in input().split()] for i in range(n)]
# spiralPrint(arr, n, m)


def mergeSort(arr):
  n = len(arr)
  if n == 0 or n == 1:
    return
  mid = n // 2
  s1, s2 = arr[:mid], arr[mid:]
  mergeSort(s1)
  mergeSort(s2)
  merge(s1, s2, arr)

def merge(li1, li2, arr):
  n, m = len(li1), len(li2)
  i, j, k = 0, 0, 0

  while i < n and j < m:
    if li1[i] <= li2[j]:
      arr[k] = li1[i]
      i += 1
    else:
      arr[k] = li2[j]
      j += 1
    k += 1
    
  while i < n:
    arr[k] = li1[i]
    i += 1
    k += 1
  while j < m:
    arr[k] = li2[j]
    j += 1
    k += 1
  

def quickSort(arr, start, end):
  if start >= end:
    return
  pi_idx = partition(arr, start, end)
  quickSort(arr, start, pi_idx-1)
  quickSort(arr, pi_idx+1, end)

def partition(arr, start, end):
  pivot = arr[start]
  count = 0
  for i in range(start, end+1):
    if arr[i] < pivot:
      count += 1
  arr[start], arr[start+count] = arr[start+count], arr[start]

  i, j = start, end
  while i < j:
    if arr[i] < pivot:
      i += 1
    elif arr[j] >= pivot:
      j -= 1
    else:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1
  
  return start+count


# arr = [int(x) for x in input().split()]
# mergeSort(arr)
# quickSort(arr, 0, len(arr)-1)
# print(arr)

def towerOfHanoi(n, src, helper, dest):
  if n == 1:
    print(f"Move 1st disk from {src} to {dest}")
    return
  towerOfHanoi(n-1, src, dest, helper)
  print(f"Move {n}th disk from {src} to {dest}")
  towerOfHanoi(n-1, helper, src, dest)

# towerOfHanoi(5, 'A', 'B', 'C')


def staircase(n):
  if n == 0 or n == 1:
    return 1
  if n == 2:
    return 2
  return staircase(n-1) + staircase(n-2) + staircase(n-3)

# s = int(input())
# print(staircase(s))

def powerOfNum(x, n):
  if n == 0:
    return 1
  s1 = powerOfNum(x, n//2)
  return s1*s1 if n%2 == 0 else x*s1*s1

# print(powerOfNum(2, 5))

# 1 sec => 10^8 operations, so ab constraints dekh ke pta lgao, kya accept hoga
# constraint => 10^6 hai, matlab O(n) chalega O(n^2) nhi chalega


