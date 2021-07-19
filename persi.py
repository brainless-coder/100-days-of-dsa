def sortAccToFreq(arr):
    freq = {}
    ans = []
    for ele in arr:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
        
    while len(freq) != 0:
        maxmVal = -1
        maxmKey = -1
        for ele in freq:
            if freq[ele] > maxmVal:
                maxmVal = freq[ele]
                maxmKey = ele
        for i in range(maxmVal):
            ans.append(maxmKey)
        del freq[maxmKey]
    
    return ans

def sortAccToFreqOpti(arr):
    freq = {}
    ans = []
    for ele in arr:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1

    freqArr = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    for ele in freqArr:
        for i in range(ele[1]):
            ans.append(ele[0])
    return ans

# arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 9, 10]
# print(sortAccToFreq(arr))
# print(sortAccToFreqOpti(arr))


def sumOfDigits(n):
    ans = 0
    while (n):
        dig = n%10
        ans += dig
        n //= 10
    return ans

def totalOrderPerClient(arr):
    ans = []
    for i in range(len(arr)):
        ans.append(sumOfDigits(arr[i]))
    return ans

arr = [43, 345, 20, 987]
print(totalOrderPerClient(arr))