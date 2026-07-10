class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val=float('-inf')
        current_total=0
        for i in range(len(nums)):
            curr_val=nums[i]
            current_total+=curr_val
            max_val=max(current_total,max_val)
            if current_total<0:
                current_total=0
        return max_val