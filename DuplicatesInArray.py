class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for _ in range(len(nums)):
            res.append(0)
        for each in nums:
            res[each-1] += 1
        nums = []
        for i in range(len(res)):
            if res[i] > 1:
                nums.append(i+1)
        return nums
