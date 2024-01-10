def lengthOfLongestSubstring(s):
    i = 0
    count = 0
    strs = list(s)
    memory = []
    length = []
    
    while i < len(strs):
        if strs[i] in memory:
            length.append(count)
            count = 1
            del memory[0:i]
            memory.append(strs[i])
        else:
            memory.append(strs[i])
            count += 1
        #print(count)
        #print(memory)
        i += 1
    length.append(count)
    return max(length)

s = "abcabcbb"
print(lengthOfLongestSubstring(s))