class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        
        """
        :type s: str
        :rtype: int
        """
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
                if ch in dic:
                    start = max(start, dic[ch]+1)
                    res = max(res, i-start+1)
                dic[ch] = i
        return res
s = "aab"
a = Solution()
b = a.lengthOfLongestSubstring(s)
print(b)