n = int(input())
mid = n//2
if n%2 == 0:
    mid -= 1
star = 1
for i in range(n):
    space = abs(mid-i)
    if n%2 == 0 and i > mid:
        space -= 1
    for j in range(space):
        print(" ", end="")
    for j in range(star):
        print("*", end="")
    if n%2 == 0 and i == mid:
        print()
        continue
    if i < mid:
        star += 2
    else:
        star -= 2  
    print()