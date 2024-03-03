class Solution(object):
    def strStr(self, haystack, needle):
        position = 0

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            #print('i = ' + str(i))
            match = True #一致しているものとして探索開始
            for j in range(len(needle)):
                if len(haystack) <= i + j:
                    match = False
                    return -1
                
                if (haystack[i + j] != needle[j]):
                    match = False #一致しなかった
                    break
                else:
                    position = i + j - (len(needle) - 1)
                if match and j == len(needle) - 1: #すべての文字が一致していれば出力
                    return position
        return -1

haystack = "leetcode"
needle = "leeto"
instance = Solution()
print(instance.strStr(haystack, needle))