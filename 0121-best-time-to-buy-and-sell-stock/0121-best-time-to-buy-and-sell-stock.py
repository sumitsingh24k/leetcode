class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val=0
        min_val=float('inf')
        for val in prices:
            min_val=min(val,min_val)
            max_val=max(max_val,val-min_val)
        return max_val