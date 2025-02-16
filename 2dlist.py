# Row wise Sum
def rowWiseSum():
    rowCol = input().split()
    n, m = int(rowCol[0]), int(rowCol[1])
    li = [[int(ele) for ele in input().split()] for i in range(n)]
    output = []
    sum = 0

    for row in li:
        for ele in row:
            sum += ele
        output.append(sum)
        sum = 0
    return output 

# t = int(input())
# while t > 0:
#     output = rowWiseSum()
#     for ele in output:
#         print(ele, end=" ")
#     print()
#     t -= 1


# Largest Column Sum
def largestColSum(li):
    n = len(li)
    m = len(li[0])
    sumArr = [0] * m
    maxSum, maxIdx = -1, -1

    # for i in range(n):
    #     for j in range(m):
    #         sumArr[j] += li[i][j]

    # for i in range(m):
    #     if sumArr[i] > maxSum:
    #         maxSum = sumArr[i]
    #         maxIdx = i

    # Iterating column wise
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += li[i][j]
        if sum > maxSum:
            maxIdx = j
            maxSum = sum

    return maxSum, maxIdx
    
# li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# larSum, larColIndex = largestColSum(li)
# print(larSum, larColIndex)


# Largest Row or Column
def largestRowCol():
    rowColInput = input().split()
    n, m = int(rowColInput[0]), int(rowColInput[1])
    li = [[int(ele) for ele in input().split()] for i in range(n)]
    maxRowSum, maxColSum, maxRowIdx, maxColIdx = -1, -1 , -1, -1

    for i in range(n):
        rowSum = 0
        for ele in li[i]:
            rowSum += ele
        if rowSum > maxRowSum:
            maxRowSum = rowSum
            maxRowIdx = i
    
    for j in range(m):
        colSum = 0
        for ele in li:
            colSum += ele[j]
        if colSum > maxColSum:
            maxColSum = colSum
            maxColIdx = j
        
    if maxRowSum >= maxColSum:
        print("Row " + str(maxColIdx) + " " + str(maxColSum))
    else:
        ans = "Column {} {}"
        ans = ans.format(maxColIdx, maxColSum)
        print(ans)

# t = int(input())
# while t > 0:
#     largestRowCol()
#     t -= 1


# Wave Print
def waveArray():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    li = [[int(j) for j in input().split()] for i in range(n)]
    ans = []
    for j in range(m):
        if j%2 == 0:
            for i in range(n):
                ans.append(li[i][j])
        else:
            for i in range(n-1, -1, -1):
                ans.append(li[i][j])
    
    for ele in ans:
        print(ele, end=" ")
    print()

t = int(input())
while t > 0:
    waveArray()
    t -= 1