class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        subs = ''
        for i in range(len(s)):
            temp = self.Palindrome(s,i,i)
            if len(temp) > len(subs):
                subs = temp
            temp = self.Palindrome(s,i,i+1) 
            if len(temp) > len(subs):
                subs = temp 
        return subs       


    def Palindrome(self,s,i,j):
        while i >=0 and j< len(s) and s[i] == s[j]:
            i-=1
            j+=1
        return s[i+1:j]
s = "babad"
print(Solution().longestPalindrome(s))