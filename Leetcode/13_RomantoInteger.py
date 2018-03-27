class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        
        res = 0
        p = 'I'
        for c in s[::-1]: # reverse the string
            if d[c] < d[p]:
                res = res - d[c]
            else:
                res = res + d[c]
            p = c 
        return res