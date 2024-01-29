class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        strs = list(s)
        memory = ""
        max_length = 0
        
        while i < len(strs):
            if strs[i] in memory:
                memory =  memory[memory.index(strs[i])+1:]

            memory = memory + strs[i]
            i += 1
            max_length = max(max_length, len(memory))
            
        return max_length


s = "abcabcbb"
instance = Solution()
print(instance.lengthOfLongestSubstring(s))