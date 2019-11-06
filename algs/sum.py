# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if x + nums[j] == target:
                    return i, j
