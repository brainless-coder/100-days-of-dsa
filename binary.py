def decimalToBinary():
    n = int(input())
    ans = []
    while n:
        i = 0
        m = 2 ** 0
        while m <= n:
            i += 1
            m *= 2
        m //= 2
        ans.append(i - 1)
        n -= m

    binaryNum = [0] * (ans[0] + 1)
    firstEle = ans[0]
    for i in range(len(ans)):
        ans[i] = firstEle - ans[i]

    for i in range(len(binaryNum)):
        if i in ans:
            binaryNum[i] = 1
    for i in range(len(binaryNum)):
        binaryNum[i] = str(binaryNum[i])

    output = "".join(binaryNum)
    print(output)


def decimalToBinaryNew():
    n = int(input())
    ans = ""
    while n:
        rem = n%2
        ans = str(rem) + ans
        n //= 2
    print(ans)


def binaryToDecimal():
    n = input()
    i, j = len(n) - 1, 0
    ans = 0
    while i >= 0:
        ans += int(n[i]) * (2**j)
        i -= 1
        j += 1
    print(ans)


# decimalToBinary()
decimalToBinaryNew()
# binaryToDecimal()
