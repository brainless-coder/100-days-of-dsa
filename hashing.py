def maxmFreq(arr):
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    maxmVal = -1
    maxmKey = -1
    for key in freq:
        if (freq[key] > maxmVal):
            maxmKey = key
            maxmVal = freq[key]
    print(maxmKey)

# O(n^2)
def pairSumTo0Naive(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == -arr[j]:
                        print(arr[i], arr[j])
                        count += 1
    print("Count: " + str(count))

# O(n) with 2 loops
def pairSumTo0(arr):
    freq = {}
    count = 0
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    
    for key in freq:
        if key < 0:
            if -key in freq:
                for i in range(freq[key]*freq[-key]):
                    print(key, -key)
                count += (freq[key]*freq[-key])
    print(count)

# O(n) with one loop
def pairSumTo0Optimized(arr):
    freq = {}
    count = 0
    for ele in arr:
        if -ele in freq:
            for i in range(freq[-ele]):
                print(ele, -ele)
            count += freq[-ele]
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
    print(count)

def extractUniqueChar(s):
    freq = {}
    ans = ""
    for char in s:
        if char not in freq:
            freq[char] = 1
            ans += char
    print(ans)

def longestConsSeq(arr):
    arr.sort()
    freq = {}
    for ele in arr:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
    print(freq)

    for key in freq:
        if key+1 in freq:
            print(key, end=" ")
        else:
            print(key)
    
        


arr = [int(x) for x in input().split()]
# maxmFreq(arr)
# pairSumTo0Naive(arr)
# pairSumTo0(arr)
# pairSumTo0Optimized(arr)
# s = input()
# extractUniqueChar(s)
longestConsSeq(arr)