# Replace character in a string
# def replace(str, char1, char2):
#     newStr = ""
#     for x in str:
#         if x == char1:
#             newStr += char2
#         else:
#             newStr += x
#     return newStr

# str = "fsafsavxz"
# str = replace(str, 's', 'd')
# print(str)


# count vowels, consonants, digits and symbols in a string
def countInString(str):
    v = c = d = s = 0
    str = str.lower()
    for x in str:
        if x >= 'a' and x <= 'z':
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                v += 1
            else:
                c += 1
        elif x >= '0' and x <= '9':
            d += 1
        else:
            s += 1
    return v, c, d, s

# str = input()
# v, c, d, s = countInString(str)
# print(v, c, d, s)


# Check Permutation
def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    # Sum of ASCII values approach
    # sum1, sum2 = 0, 0
    # for x in str1:
    #     sum1 += ord(x)
    # for x in str2:
    #     sum2 += ord(x)

    # if sum1 == sum2:
    #     return True
    # return False

    # counting frequency of each char
    frequency = [0] * 256
    for x in str1:
        ch = ord(x)
        frequency[ch] += 1
    for x in str2:
        ch = ord(x)
        frequency[ch] -= 1
    for i in range(256):
        if frequency[i] != 0:
            return False
    return True

# str1 = input()
# str2 = input()
# print(isPermutation(str1, str2))


# Remove Consecutive Duplicates
def removeconsDup(string):
    start, end = 0, len(string)
    newStr = ""
    while start < end:
        uniqueChar = string[start]
        uniqueCharIndex = start+1
        while (uniqueCharIndex < end and string[uniqueCharIndex] == uniqueChar):
            uniqueCharIndex += 1
        
        newStr += uniqueChar
        start = uniqueCharIndex
        
    return newStr

# string = input()
# string = removeconsDup(string)
# print(string)


# Reverse Each Word
def reverseEachWord(string):
    # string = string.split()
    # newStr = ""
    # for ele in string:
    #     ele = ele[::-1]
    #     newStr += ele + " "
    # return newStr
    return " ".join(x[::-1] for x in string.split())
    
# string = input()
# string = reverseEachWord(string)
# print(string)


# Remove character
def removeCharacter(string, ch):
    # return string.replace(ch, '')
    newStr = ""
    for ele in string:
        if ele != ch:
            newStr += ele
    return newStr

# string = input()
# ch = input()
# string = removeCharacter(string, ch)
# print(string)


# Highest Occuring Character
def highestOccuringChar(string):
    freq = [0] * 256
    maxFreq = 0

    for i in range(len(string)):
        freq[ord(string[i])] += 1
        maxFreq = max(maxFreq, freq[ord(string[i])])

    answer = '\0'

    for i in range(len(string)):
        if maxFreq == freq[ord(string[i])]:
            answer = string[i]
            break

    return answer

# string = input()
# string = highestOccuringChar(string)
# print(string)


# Compress The String
def compress(string):
    count = 1
    newStr = ""

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            if count > 1:
                newStr += string[i] + str(count)
            else:
                newStr += string[i]
            count = 1

    if count > 1:
        newStr += string[len(string)-1] + str(count)
    else:
        newStr += string[len(string)-1]
    return newStr
    

string = input()
string = compress(string)
print(string)