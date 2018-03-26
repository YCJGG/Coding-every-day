class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        memo = {}
        def dp(i,j):
            if (i,j) not in memo:
                # 判断为空的字符串，若都为空，返回True
                # 结束条件
                if j == len(p):
                    ans = i == len(s)
                else:
                    #寻找第一个匹配的字符
                    first_match = i < len(s) and p[j] in {s[i],"."}
                    #处理出现*号的情况
                    if j+1 < len(p) and p[j+1] == '*':
                        #判断*号后面是否为第一个匹配的字符 or 判断*号能否代替匹配的字符
                        ans = dp(i ,j+2) or first_match and dp(i+1,j)
                    else:
                        
                        ans = first_match and dp(i+1,j+1)
                memo[i,j] = ans
                print(memo)
            return memo[i,j]
        return dp(0,0)       

s = 'aab'
p = 'c*a*b'        
print(Solution().isMatch(s,p))