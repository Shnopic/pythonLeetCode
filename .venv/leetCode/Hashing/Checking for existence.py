#Example 1: 1. Two Sum
#Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:  # This operation is O(1)!
                return [i, dic[complement]]

            dic[num] = i

        return [-1, -1]


#Example 2: 2351. First Letter to Appear Twice
#Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "


#Example 3: Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
def find_numbers(nums):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)

    return ans