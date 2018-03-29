class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        temp = 1e10
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while(l<r):
                s = nums[i] + nums[l] + nums[r] - target
                # print('1',i)
                # print('2',l)
                # print('3',r)
                if s < 0:
                    
                    if s*(-1) < temp:
                        res = nums[i] + nums[l] + nums[r]
                        temp = s*(-1)
                    l +=1
                elif s > 0:
                    
                    if s < temp:
                        res = nums[i] + nums[l] + nums[r]
                        print(res)
                        temp = s
                    r-= 1
                else:
                    return nums[i] + nums[l] + nums[r]
                    # while l < r and nums[l] == nums[l+1]:
                    #     l+=1
                    # while l < r and nums[r] == nums[r-1]:
                    #     r-=1
                    # l+=1 
                    # r-= 1
        
        return res

nums = [0,1,2]
target = 0
print(Solution().threeSumClosest(nums, target))