#You are given a 0-indexed array nums of n integers, and an integer k.
#The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1
#Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
#The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part

class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix = [nums[0]]
        n = len(nums)
        s = []
        x = k*2+1
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        for i in range(0, n):
            if (i-k) < 0 or (i + k) > n-1:
                s.append(-1)
            else:
                s.append((prefix[i+k] - prefix[i-k] + nums[i-k])/(x))
        return s