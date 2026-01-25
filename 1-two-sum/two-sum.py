class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i,val in enumerate(nums):
            curr_val=target-val
            if curr_val in dictionary:
                return [dictionary[curr_val],i]
            dictionary[val]=i
    