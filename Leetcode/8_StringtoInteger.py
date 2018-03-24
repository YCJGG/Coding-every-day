class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        i = 0
        result = 0
        flag = 1
        
        if len(s)==0:
            return 0

        while(s[i]==' '):
            i+=1
        
        if s[i] =='+':
            flag = 1
            i += 1
            if i == len(s):
                return 0
        
        elif s[i] == '-':
            flag = -1
            i+= 1
            if i == len(s):
                return 0

        while(i<len(s)):
            if s[i] in dict:
                result = result*10 + int(s[i])
                i += 1
            else:
                break
        
        if flag*result >2**31-1:
            return 2**31-1
        if flag*result <-2**31:
            return -2**31
        return flag*result
s = "2147483648"
a = Solution().myAtoi(s)
print(a)