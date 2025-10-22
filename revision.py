import random

def isListSortedUsingRecursion(li, si=0):
	n = len(li)
	if si == n or si == n-1:
		return True
	
	isSmallSorted = isListSortedUsingRecursion(li, si+1)
	if isSmallSorted and li[si] <= li[si+1]:
		return True
	return False 


def firstIndexOfNum(li, x, fi=0):
	n = len(li)
	if fi == n:
		return -1
	
	if li[fi] == x:
		return fi
	return firstIndexOfNum(li, x, fi+1)


def lastIndexOfNum(li, x, i=0):
	n = len(li)
	if i == n:
		return -1
	
	idx = lastIndexOfNum(li, x, i+1)
	if idx == -1 and li[i] == x:
		return i
	return idx


def insertionSort(li):
	n = len(li)
	for i in range(1, n):
		key = li[i]
		j = i-1

		# j-- karo, aur wo saare elements jo key se baare hai, unhe ek aage karte jao
		while j >= 0 and key < li[j]:
			li[j+1] = li[j]
			j -= 1
		li[j+1] = key
	print(li)


def merge(l1, l2):
	m, n = len(l1), len(l2)
	arr = []

	i, j = 0, 0
	while i < m and j < n:
		if l1[i] <= l2[j]:
			arr.append(l1[i])
			i += 1
		else:
			arr.append(l2[j])
			j += 1

	while i < m:
		arr.append(l1[i])
		i += 1
	
	while j < n:
		arr.append(l2[j])
		j += 1

	return arr

def mergeSort(li):
	n = len(li)
	if n <= 1:
		return li

	mid = n//2
	l1 = mergeSort(li[:mid])
	l2 = mergeSort(li[mid:])
	return merge(l1, l2)


def partition(arr, si, ei):
	# pick a element as pivot
	pivot = random.choice(arr[si:ei+1])
	# pivot = arr[si]
	count = 0
	for i in range(si, ei+1):
		if arr[i] < pivot:
			count += 1
	# place it at its correct position
	arr[si], arr[si+count] = arr[si+count], arr[si]
	pivot_index = si + count
	# ab < and >= ko shi se karo, (i, j) ka use karke
	i, j = si, ei
	while i < j:
		if arr[i] < pivot:
			i += 1
		elif arr[j] >= pivot:
			j -= 1
		else:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1
	return pivot_index

def quickSort(arr, si, ei):
	if si >= ei:
		return
	pi = partition(arr, si, ei)
	quickSort(arr, si, pi-1)
	quickSort(arr, pi+1, ei)


def countSort(arr):
	mx, mn = max(arr), min(arr)
	freq = [0]*(mx-mn+1)
	n = len(arr)

	# making the freq array
	for i in range(n):
		freq[arr[i]-mn] += 1

	# Calculating prefix sum of freq array
	for i in range(1, mx-mn+1):
		freq[i] += freq[i-1]

	# freq arr me -1 kardo sab ele se, taaki apne ko shi index mil jaaye sabka
	for i in range(mx-mn+1):
		freq[i] -= 1

	ans = [0]*n
	for i in range(n-1, -1, -1):
		ans[freq[arr[i]-mn]] = arr[i]
		freq[arr[i]-mn] -= 1
	
	print(ans)



li = [int(x) for x in input().split()]
# x = int(input())
# print(isListSortedUsingRecursion(li))
# print(isListSortedUsingRecursion(li))
# print(firstIndexOfNum(li, x))
# print(lastIndexOfNum(li, x))
# insertionSort(li)
# print(mergeSort(li))
# quickSort(li, 0, len(li)-1)
countSort(li)
# print(li)