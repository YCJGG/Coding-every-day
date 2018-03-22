class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Limit Exceeded
        # for i in range(len(nums)-1):
        #     j = i + 1
        #     while(j<len(nums)):
        #         result = nums[i] + nums[j]
        #         if result == target:
        #             return[i,j]
        dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict:
                return [dict[target - nums[i]],i]
            if nums[i] not in dict:
                dict[nums[i]] = i  

        #由于题目说了有且只有唯一解，可以考虑两遍扫描求解：第一遍扫描原数组，
        # 将所有的数重新存放到一个dict中，
        # 该dict以原数组中的值为键，原数组中的下标为值；第二遍扫描原数组，
        # 对于每个数nums[i]查看target-nums[i]是否在dict中，若在则可得到结果。 