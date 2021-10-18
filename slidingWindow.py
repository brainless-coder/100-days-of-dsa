def occOfAnagram(s, ptr):
    count = 0
    k = len(ptr)
    size = len(s)
    ptrFreq = {}
    strFreq = {}
    for char in ptr:
        ptrFreq[char] = ptrFreq.get(char, 0) + 1
    
    i, j = 0, 0
    while j < size:
        strFreq[s[j]] = strFreq.get(s[j], 0) + 1
        if j-i+1 == k:
            if strFreq == ptrFreq:
                count += 1
            strFreq[s[i]] -= 1
            if strFreq[s[i]] == 0:
                strFreq.pop(s[i])
            i += 1
        j += 1
    return count



s = input()
ptr = input()
print(occOfAnagram(s, ptr))