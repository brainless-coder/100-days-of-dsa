
# O(n^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break
    print(arr)

# O(n^2)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(arr)

# O(n^2)
def insertionSort(arr):
    n = len(arr)
    i = 1
    while i < n:
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    print(arr)

# O(nlong)
def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    mid = len(arr)//2
    li1 = mergeSort(arr[:mid])
    li2 = mergeSort(arr[mid:])
    arr = merge(li1, li2, arr)
    return arr

# O(n+m)
def merge(li1, li2, arr):
    n, m = len(li1), len(li2)
    arr = [0 for i in range(n+m)]
    i, j, k = 0, 0, 0

    while i < n and j < m:
        if li1[i] < li2[j]:
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
    
    return arr
    

def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = partition(arr, start, end)
    quickSort(arr, start, pivot-1)
    quickSort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = start
    i = start
    count = 0
    while i <= end:
        if arr[i] < arr[pivot]:
            count += 1
        i += 1
    arr[pivot], arr[start+count] = arr[start+count], arr[pivot]
    pivot = start+count
    i, j = start, end
    while i < j:
        if arr[i] > arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    return pivot


arr = [int(x) for x in input().split()]
n = len(arr)
# bubbleSort(arr)
# selectionSort(arr)
# insertionSort(arr)
# print(mergeSort(arr))
quickSort(arr, 0, n-1)
print(arr)



def binarySearch(arr, x):
    n = len(arr)
    start, end = 0, n-1
    
    for i in range(n):
        mid = (start + end) // 2
        if x > arr[i]:
            start = mid + 1
        elif x < arr[i]:
            end = mid - 1
        else:
            return True
    return False

# print(binarySearch([1, 2, 5, 8, 12, 15, 18], 1))


