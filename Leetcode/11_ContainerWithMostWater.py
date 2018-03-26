class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max = 0
        while(i<j):
            area = min(height[i],height[j])*(j - i)
            print(i,j)
            #print(area)
            if area > max:
                max = area
            k = i
            if height[i] < height[j]:
                i+=1
            if height[k]>=height[j]:
                j-=1
        return max
height = [2,3,10,5,7,8,9]
a =  Solution().maxArea(height)
print(a)