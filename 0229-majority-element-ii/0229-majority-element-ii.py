class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        counter=Counter(nums)
        target=len(nums)/3
        result=[]
        for key,val in counter.items():
            if val>target:
                result.append(key)
        return result