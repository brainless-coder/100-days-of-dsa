# O(nlogn)
def naive(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def optimisedHashmapApproach(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}
    for char in range(len(s1)):
        freq1[s1[char]] = freq1.get(s1[char], 0) + 1
        freq2[s2[char]] = freq2.get(s2[char], 0) + 1
    
    for key in freq1:
        if freq1.get(key) != freq2.get(key):
            return False
    return True

def optimisedStringHashmap(s1, s2):
    if len(s1) != len(s2):
        return False

    count1 = [0] * 256
    count2 = [0] * 256
    for char in range(len(s1)):
        count1[ord(s1[char])] += 1
        count2[ord(s2[char])] += 1
    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True

def optimisedStringHashmapSingleArray(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for i in range(256):
        if count[i] != 0:
            return False
    return True



s1 = input()
s2 = input()
print(naive(s1, s2))
print(optimisedHashmapApproach(s1, s2))
print(optimisedStringHashmap(s1, s2))
print(optimisedStringHashmapSingleArray(s1, s2))