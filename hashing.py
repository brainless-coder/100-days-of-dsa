
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

    ans = []
    for key in freq:
        if key+1 in freq:
            ans.append(key)
        else:
            ans.append(key)
            ans.append(0)

    count = 0
    countArr = []
    for i in range(len(ans)-1):
        if ans[i+1] != 0:
            count += 1
        else:
            countArr.append(count)
            count = 0
    
    maxIndex = 0
    maxm = -1
    for i in range(len(countArr)):
        if countArr[i] > maxm:
            maxm = countArr[i]
            maxIndex = i
    
    i = 0
    while(maxIndex != 0):
        if ans[i] == 0:
            maxIndex -= 1
        i += 1

    print(ans[i], end=" ")
    print(ans[i+maxm-1])
    
def longestConsSeqOpti(arr):
    traversed = {}
    maxLength, start = -1 , 0
    for ele in arr:
        traversed[ele] = False
    
    for ele in arr:
        count = 0
        temp = ele
        if traversed[temp] == False:
            traversed[temp] = True
            count += 1
            while temp+1 in traversed:
                traversed[temp+1] = True
                count += 1
                temp += 1
            temp = ele
            while temp-1 in traversed:
                traversed[temp-1] = True
                count += 1
                temp -= 1
            if count > maxLength:
                start = temp
                maxLength = count

    for i in range(maxLength):
        print(start+i, end=" ")
    
        


arr = [int(x) for x in input().split()]
# maxmFreq(arr)
# pairSumTo0Naive(arr)
# pairSumTo0(arr)
# pairSumTo0Optimized(arr)
# s = input()
# extractUniqueChar(s)
# longestConsSeq(arr)
longestConsSeqOpti(arr)