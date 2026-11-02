class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_val=float('-inf')
        current_val=0
        for i in range(len(nums)):
            current_val+=nums[i]
            max_val=max(current_val,max_val)
            if current_val<0:
                current_val=0
        return max_val