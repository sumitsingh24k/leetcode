class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def total(goal):
            if goal<0:
                return 0
            left=0
            n=len(nums)
            count=0
            curr_sum=0
            for right in range(n):
                curr_sum+=nums[right]
                while curr_sum>goal:
                    curr_sum-=nums[left]
                    left+=1
                count+=right-left+1
            return count
        return total(goal)-total(goal-1)