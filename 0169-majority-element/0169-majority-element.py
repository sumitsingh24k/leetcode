class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        n=len(nums)
        for key,val in freq.items():
            if val>(n/2):
                return key