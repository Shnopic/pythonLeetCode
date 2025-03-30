#Given an array of integers nums, you start with an initial positive value startValue.
#In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#Return the minimum positive value of startValue such that the step by step sum is never less than 1.

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [nums[0]]
        m = prefix[0]
        for i in range (1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            m = min(m, prefix[-1])
        if m <= 0:
            return abs(m)+1
        else:
            return 1