class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val=0
        max_val=max(nums)
        for num in nums:
            min_val+=max_val-num
        return min_val