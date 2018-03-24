class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        input = x
        if x < 0:
            return False
        result = 0
        while (x!=0):
            r = x%10
            result = result*10 + r
            x = x // 10
        
        if input == result:
            return True
        else:
            return False

s = 1
a = Solution().isPalindrome(s)
print(a)
        