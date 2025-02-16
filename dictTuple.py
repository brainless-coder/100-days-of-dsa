# Print all words with frequency K
def printKFreqWords(s, k):
    freq = {}
    s = s.split()
    for word in s:
        freq[word] = freq.get(word, 0) + 1
    for ele in freq:
        if freq[ele] == k:
            print(ele)

# s = "this is a word string having many many word"
# k = int(input())
# printKFreqWords(s, k)


# Sum of Unique nos in a list
def uniqueSum(li):
    s = set()
    sum = 0
    for ele in li:
        s.add(ele)
    for ele in s:
        sum += ele
    return sum

# li = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 4]
# print(uniqueSum(li))


# First Repeating character
def firstRepeatingchar(s):
    freq = {}
    for ele in s:
        a = ele.lower()
        if freq.get(a) == 1:
            return ele
        freq[a] = freq.get(a, 0) + 1
    return s[0]


# First non-repeating character
def nonRepeatingChar(s):
    freq = {}
    for ele in s:
        freq[ele] = freq.get(ele, 0) + 1
    for ele in freq:
        if freq[ele] == 1:
            return ele
    return s[0]

# s = input()
# print(firstRepeatingchar(s))
# print(nonRepeatingChar(s))


# Extract Unique characters
def uniqueChar(s):
    char = {}
    ans = ""
    for ele in s:
        if ele not in char:
            char[ele] = True
            ans += ele
    return ans

# s = input()
# print(uniqueChar(s))


# Different Names
def differentNames(s):
    s = s.split()
    freq = {}
    ans = ""
    for name in s:
        freq[name] = freq.get(name, 0) + 1
    for name in freq:
        if freq[name] > 1:
            ans += name + " " + str(freq[name]) + "\n"
    if ans == "":
        return -1
    else:
        return ans

# s = input()
# print(differentNames(s))


# Maximum Frequency Number
def maxfreqNum(li):
    freq = {}
    ans = li[0]
    for ele in li:
        freq[ele] = freq.get(ele, 0) + 1
    for ele in freq:
        if freq[ele] > freq[ans]:
            ans = ele
    return ans

li = [int(x) for x in input().split()]
print(maxfreqNum(li))