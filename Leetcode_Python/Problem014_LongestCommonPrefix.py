class Solution(object):
    def longestCommonPrefix(self, strs):
        answer = ""
        rows = list(zip(*strs))
        for i in rows:
            if len(set(i)) == 1:
                answer = answer + i[0]
            else:
                break       
        return answer
    
strs = ["flower","flow","flight"]
instance = Solution()
print(instance.longestCommonPrefix(strs))