from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counting=Counter(nums)
        for key,val in counting.items():
            if val ==1:
                return key