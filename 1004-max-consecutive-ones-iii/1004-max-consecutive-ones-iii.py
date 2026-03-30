class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count=0
        left=0
        right=0
        zero_count=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_count=max(max_count,(right-left)+1)
            right+=1
        return max_count