#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        s = []
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                s.append(nums[left] **2)
                left += 1
            else:
                s.append(nums[right] **2)
                right -= 1
        return s[::-1]