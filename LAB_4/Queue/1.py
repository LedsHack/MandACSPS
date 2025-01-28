def firstUniqChar(s):
    freq = {}
    for i, char in enumerate(s):
        if char not in freq:
            freq[char] = [1, i]
        else:
            freq[char][0] += 1
    for count, index in freq.values():
        if count == 1:
            return index
    return -1
print(firstUniqChar("leopard"))
print(firstUniqChar("loveleopard"))
print(firstUniqChar("aabb"))
