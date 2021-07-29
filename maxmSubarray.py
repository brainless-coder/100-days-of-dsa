def subArrayNaive(arr):
    globalMaxm = -90000
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            maxm = 0
            for k in range(i, j+1):
                maxm += arr[k]
                if maxm > globalMaxm:
                    globalMaxm = maxm
    return globalMaxm

def kadaneAlgo(arr):
    maxSum = -9000
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]
        if currSum > maxSum:
            maxSum = currSum
        if currSum < 0:
            currSum = 0
    return maxSum


arr = [int(x) for x in input().split()]
# print(subArrayNaive(arr))
print(kadaneAlgo(arr))