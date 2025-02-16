# Check if fibonacci or not
# def fibonacci(n):
#     prev , curr = 0, 1
#     while curr < n:
#         temp = prev + curr
#         prev = curr
#         curr = temp
#     if (curr == n):
#         return True
#     else:
#         return False

# n = int(input())
# print(fibonacci(n))


# Check Armstrong
"""
An Armstrong number is a number (with digits n) 
such that the sum of its digits raised to nth power is equal to the number itself.

For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
"""
def armstrong(n):
    m = n
    digits = ans = 0
    while m:
        m //= 10
        digits += 1
    m = n
    while m:
        a = m % 10
        m //= 10
        ans += (a**digits)
    # print(ans)
    if ans == n:
        return True
    else:
        return False
    



n = int(input())
print(armstrong(n))
