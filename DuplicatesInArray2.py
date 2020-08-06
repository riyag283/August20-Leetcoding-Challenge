class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            nums[abs(int(nums[i]))-1] = int(nums[abs(int(nums[i]))-1])*-1
        for i in range(len(nums)):
            if type(nums[i]) != str:
                if nums[i] > 0:
                    res.append(i+1)
        return res
