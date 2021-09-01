def generateSubstring(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            print(s[i:j])

def findsubstring(s1, s2):
    n1, n2 = len(s1), len(s2)
    s2Freq = {}
    ans = []
    for char in s2:
        s2Freq[char] = s2Freq.get(char, 0) + 1
    
    for i in range(n1):
        for j in range(i+1, n1+1):
            subStr = s1[i:j]
            s1Freq = {}
            for char in subStr:
                s1Freq[char] = s1Freq.get(char, 0) + 1
            if s2Freq.items() <= s1Freq.items():
                ans.append(subStr)
    
    if len(ans) > 0:
        ans.sort(key=len)
        print(ans[0])
    else:
        print()


# s1, s2 = input(), input()
# generateSubstring(s1)
# findsubstring(s1, s2)


def minmSets(s, y):
    count = 0
    flag = False
    num = 0
    l = len(s)

    for i in range(len(s)):
        num = num*10 + ord(s[i]) - ord('0')
        if num <= y:
            flag = True
        else:
            if flag:
                count += 1
            
            num = ord(s[i]) - ord('0')
            flag = False

            if num <= y:
                flag = True
            else:
                num = 0
        
    if flag:
        count += 1

    print(count)    

# s = input()
# y = int(input())
# minmSets(s, y)

def countBits(n):
    count = 0
    while n:
        rem = n%2
        if rem:
            count += 1
        n //= 2

    return count

def sortByBits(arr):
    # Create a list of tuples of (countBits, val)
    # ints = [(countBits(val), val) for val in arr]  
    ints = []   
    for ele in arr:
        ints.append((countBits(ele), ele)) 

    # Sort the list of tuples first by bits, then by val
    ints.sort()

    # Create a list of the values in the sorted list
    # results = [val for num_ones, val in ints]
    # print(results)

    ans = []
    for ele in ints:
        print(ele[1], end=" ")


# li = [int(x) for x in input().split()]
# sortByBits(li)