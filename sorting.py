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


def mergeSort(arr):
    if len(arr) == 0:
        return
    mid = len(arr)//2
    li1 = mergeSort(arr[:mid])
    li2 = mergeSort(arr[mid:])
    arr = merge(li1, li2)

# O(n+m)
def merge(li1, li2):
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
    
    print(arr)



# arr = [int(x) for x in input().split()]
# bubbleSort(arr)
# selectionSort(arr)
# insertionSort(arr)
li1 = [int(x) for x in input().split()]
li2 = [int(x) for x in input().split()]
merge(li1, li2)