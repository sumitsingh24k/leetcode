class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val=float('-inf')
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            if nums[i]==0:
                max_val=max(max_val,count)
                count=0
        return max(max_val,count)