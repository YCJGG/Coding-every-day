class Solution(object):
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i


        return max_length

#解题思路：使用一个哈希表，记录字符的索引。例如对于字符串'zwxyabcabczbb'，
# 当检测到第二个'a'时，由于之前已经有一个'a'了，所以应该从第一个a的下一个字符重新开始测算长度