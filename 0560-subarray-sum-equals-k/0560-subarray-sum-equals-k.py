class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            required=prefix_sum-k
            
            if required in mp:
                count+=mp[required]
            mp[prefix_sum]=mp.get(prefix_sum,0)+1
        return count
     