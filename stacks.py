import queue

def balancedParenthesis(s):
    st = []
    for ele in s:
        if ele == '(':
            st.append(ele)
        else:
            if (not st or st[-1] != '('):    # not st list empty hai ya nhi bta dega
                return False
            st.pop()
            
    if len(st) == 0:
        return True
    return False

def reverseStack(s1, s2):
    n = s1.qsize()
    if n <= 1:
        return s1
    while s1.qsize() > 1:
        s2.put(s1.get())
    ele = s1.get()
    while not s2.empty():
        s1.put(s2.get())
    reverseStack(s1, s2)
    s1.put(ele)

def reverseStack2(s1, s2):
    n = s1.qsize()
    if n == 0 or n == 1:
        return s1
    x = s1.get()
    reverseStack2(s1, s2)
    while not s1.empty():
        s2.put(s1.get())
    s1.put(x)
    while not s2.empty():
        s1.put(s2.get())

def redundantBrackets(string):
    s1 = []
    for char in string:
        if char == ')':
            count = 0
            while s1[-1] != '(':
                s1.pop()
                count += 1
            if count <= 1:
                return True
            s1.pop()
        else:
            s1.append(char)
    return False

def stockSpan(stockPrice):
    n = len(stockPrice)
    stockSpan = []
    for i in range(n):
        count = 1
        for j in range(i-1, -1, -1):
            if stockPrice[j] < stockPrice[i]:
                count += 1
            else:
                break
        stockSpan.append(count)    
    return stockSpan

def minBracketReversal(exp):
    n = len(exp)
    if n%2 != 0:
        return -1
    s = []
    for char in exp:
        if char == '{':
            s.append(char)
        else:
            if len(s) == 0 or s[-1] == '}':
                s.append(char)
            else:
                s.pop()
    count = 0
    while len(s) != 0:
        c1 = s.pop()
        c2 = s.pop()
        if c1 == c2:
            count += 1
        else:
            count += 2
    return count
            

s = input()
# print(balancedParenthesis(s))
# print(redundantBrackets(s))
print(minBracketReversal(s))
# stockPrice = [int(x) for x in input().split()]
# ans = stockSpan(stockPrice)
# print(ans)
# n = int(input())
# s1 = queue.LifoQueue(n)
# s2 = queue.LifoQueue()
# st = [s1.put(int(x)) for x in input().split()]
# reverseStack(s1, s2)
# reverseStack2(s1, s2)

# while not s1.empty():
#     print(s1.get(), end=" ")

