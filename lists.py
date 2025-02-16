# Array Sum

# def arraySum(li):
#     sum = 0
#     for ele in li:
#         sum += ele
#     return sum

# n = int(input())
# li = [int(x) for x in input().split()]
# print(arraySum(li))


# Swap Alternate
'''
t = int(input())
while t>0:
    n = int(input())
    li = [int(x) for x in input().split()]

    # if n%2 == 0:
    #     for i in range(0, n, 2):
    #         li[i], li[i+1] = li[i+1], li[i]
    # else:
    #     for i in range(0, n-1, 2):
    #         li[i], li[i+1] = li[i+1], li[i]

    if n%2 != 0:
        n -= 1
    li[:n:2], li[1:n:2] = li[1:n:2], li[:n:2]

    for ele in li:
        print(ele, end=" ")
    print()
    t -= 1
'''


# Find Unique
'''
t = int(input())
while t>0:
    ans = 0
    n = int(input())
    li = [int(x) for x in input().split()]
    for ele in li:
        ans = ele ^ ans
    print(ans)
    t -= 1
'''


# Find Duplicate
'''
t = int(input())
while t>0:
    ans = -1
    n = int(input())
    li = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(i+1, n):
            if li[i] == li[j]:
                ans = li[i]
                break
        if ans == li[i]:
            break
    print(ans)
    t -= 1
'''


# Array Intersection
'''
t = int(input())
while t>0:
    n = int(input())
    li1 = [int(x) for x in input().split()]
    m = int(input())
    li2 = [int(x) for x in input().split()]
    ans = []

    for ele1 in li1:
        for ele2 in li2:
            if ele1 == ele2:
                li2.remove(ele2)
                ans.append(ele1)
                break

    for ele in ans:
        print(ele, end=" ")
    print()
    t -= 1
'''

