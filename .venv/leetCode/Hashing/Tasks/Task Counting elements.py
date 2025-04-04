#Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        seen = set(arr)
        count = 0
        for i in range (len(arr)):
            if (arr[i] + 1) in seen:
                count += 1
        return count