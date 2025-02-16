n = int(input())


'''
****
***
**
*
'''
# for i in range(1, n+1):
#     for j in range( n-i+1):
#         print('*', end="")
#     print()


'''
# 1234
# 123
# 12
# 1
'''
# i = 1
# while i <= n:
#     j = 1
#     while j <= n-i+1:
#         print(j, end="")
#         j += 1
#     i += 1
#     print()


# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("#", end="")
#         j += 1
#     print()
#     i += 1


'''
   *
  **
 ***
****
'''
# i = 1
# while i <= n:
#     j = 1
#     while (j <= n):
#         if j <= n-i:
#             print(" ", end="")
#         else:
#             print('*', end="")
#         j += 1
#     print()
#     i += 1


'''
   1
  121
 12321
1234321
'''
# i = 1
# mid = n+1//2
# while i <= n:
#     count = 1
#     j = 1
#     while (j <= 2*n-1):
#         if j <= n-i:
#             print(" ", end="")
#         else:
#             print(count, end="")
#             if j < mid:
#                 count += 1
#             else:
#                 if count == 1:
#                     break
#                 count -= 1
#         j += 1
#     print()
#     i += 1


# Prime Numbers
# flag = True
# if n == 1:
#     print("Not Prime")
# for i in range(2, n):
#     if n%i == 0:
#         flag = False
#         break
# if flag:
#     print("Prime")
# else:
#     print("Not Prime")


def isPrime(n):
    if n <= 1:
        print("Not Prime")
    for i in range(2, n):
        if n%i == 0:
            break
    else:
        return True
    return False

print(isPrime(n))

# Prime numbers from 2 to N


'''
   1
  232
 34543
4567654
'''
# for i in range(1, n+1):
#     count = i
#     for j in range(1, 2*n):
#         if j <= n-i:
#             print(" ", end="")
#         else:
#             print(count, end="")
#             if j < n:
#                 count += 1
#             else:
#                 if i == count:
#                     break
#                 count -= 1
#     print()

