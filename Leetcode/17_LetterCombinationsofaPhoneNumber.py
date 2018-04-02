class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dict = {'1':'','2':"abc",'3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(dict[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        addition = dict[digits[-1]]
        print(addition)
        print(prev)
        return [s + c for s in prev for c in addition]
Solution().letterCombinations('2345')

        #递归 
        #1# 首先找到第一个字母
        #2#addition 找到prev之后的下一字母
        #3# prev = combine prev and addition 
        #4# 递归下一次，找到addition 的下一字母
        #5#重复3