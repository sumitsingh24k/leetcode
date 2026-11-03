class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        max_val=1
        count=1
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
                max_val=max(max_val,count)
            elif nums[i] == nums[i-1]:
                continue
            else:
                count=1
        return max_val