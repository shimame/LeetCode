class Solution(object):
    def longestPalindrome(self, s):
        max_strings = ""
        for i in range(len(s)):
            tmp = self.search_strings(s, i, i) #真ん中の文字(s[i])を境に左右対称
            if len(tmp) > len(max_strings):
                max_strings = tmp
            tmp = self.search_strings(s, i, i+1) #文字(s[i],s[i+1])を境に左右対称
            if len(tmp) > len(max_strings):
                max_strings = tmp
        return max_strings

    def search_strings(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]


isinstance = Solution()
s0 = "babad"
s1 = "cbbd"
print(isinstance.longestPalindrome(s0))
print(isinstance.longestPalindrome(s1))