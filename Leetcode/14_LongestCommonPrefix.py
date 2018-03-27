class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        flag = True
        prefix = min(strs, key = len)
        for i ,ch in enumerate(prefix):
            for other in strs:
                if other[i] != ch:
                    return prefix[:i] 
        return prefix
        # for i in range(0,len(strs)):
        #     for k in range(len(prefix)):
        #         if prefix[k] != strs[i][k]:
        #             flag = False
        #     if flag == False:
        #         prefix = prefix[:-1]
        #     print(i,prefix)
        # return prefix
                    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))