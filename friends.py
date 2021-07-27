def main():
    n = int(input())
    req = [int(x) for x in input().split()]
    stock = [int(x) for x in input().split()]

    ans = [0]*n
    for i in range(len(req)):
        ans[i] = stock[i] // req[i]

    print(min(ans))