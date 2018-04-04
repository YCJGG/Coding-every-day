class Solution(object):
    def threeSum(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
             
                while(l<r):
                    s =  nums[l] + nums[r]
                    print(s)
                    if s < t:
                        l +=1
                        
                    elif s > t:
                        r-= 1
                
                    else:
                        print(i)
                        res.append([nums[i],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1 
                        r-= 1
        print(res)
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # solution based on three sum
        results = []
        nums.sort()
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                three_results = self.threeSum(nums[i+1:], target - nums[i])
                for item in three_results:
                    results.append([nums[i]]+item)
        return results

    
print(Solution().fourSum([0,0,0,0],0))
