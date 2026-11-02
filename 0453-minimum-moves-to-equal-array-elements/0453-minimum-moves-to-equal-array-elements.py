class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val=min(nums)
        count=0
        for num in nums:
            count+=num-min_val
        return count