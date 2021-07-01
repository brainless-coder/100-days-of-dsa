def minimumOccurence(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    minmKey = ''
    minmVal = 10000
    for key in freq:
        if freq[key] < minmVal:
            minmKey = key
            minmVal = freq[key]
    print(minmKey)

def minOccWithoutMap(s):
    count = [0] * 256
    result = ''
    min = 10000

    for i in range(len(s)):
        count[ord(s[i])] += 1
    for char in s:
        if count[ord(char)] < min:
            min = count[ord(char)]
            result = char
    
    print(result)


def johnPassword(password):
    if len(password) < 6:
        print("Invalid password, try again")
        return
    else:
        isUpper, isLower, isDigit, space, slash = [False] * 5
        for char in password:
            if char.isupper():
                isUpper = True
            elif char.islower():
                isLower = True
            elif char.isdigit():
                isDigit = True
            elif char == " ":
                space = True
            elif char == "/":
                slash = True
        
        if isUpper and isLower and isDigit and not space and not slash:
            print("password valid")
        else:
            print("Invalid password, try again")


         
s = input()
# minimumOccurence(s)
# minOccWithoutMap(s)
johnPassword(s)