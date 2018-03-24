class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        flag = 1
        if x< 0:
            flag = -1
            x = -x
        while (x != 0):
            r = x%10
            result = result*10 + r
            x = x // 10  
        
        new_result =   flag*result
    
        if result >= 2**31:
            return 0
        return new_result

x = -2147483412
print(x>=2**30)
print(Solution().reverse(x))