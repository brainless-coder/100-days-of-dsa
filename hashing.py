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

def pairSumTo0(arr):
    neg = []
    for ele in arr:
        if ele < 0:
            neg.append(ele)
    
    for ele in neg:
        pass

arr = [int(x) for x in input().split()]
maxmFreq(arr)