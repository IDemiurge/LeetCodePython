# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:

    def removeDuplicates(self, nums) -> int:
        for n, val in enumerate(nums):
            for i, val2 in enumerate(nums[n + 1:]):
                if val2 == val:
                    nums.pop(i + 1)
        return nums

    print(removeDuplicates(None, [1, 1, 2, 2, 3, 1, 1, 2, 2, 3, 5]))
