class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)
        mid=(left+right)//2
        value=nums[mid]
        count=0
        for num in nums:
            count+=abs(value-num)
        return count