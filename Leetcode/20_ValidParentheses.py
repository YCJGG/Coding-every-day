class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n%2 !=0:
            return False
        for _ in range(n/2):
            s = s.replace('()','').replace('[]','').replace('{}','')
        #print(s)
        if s =='':
            return True
        else:
            return False
        