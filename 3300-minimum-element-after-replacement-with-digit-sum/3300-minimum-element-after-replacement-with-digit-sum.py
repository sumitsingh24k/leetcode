class Solution:
    def minElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        minimum=float('inf')
        for n in nums:
            value = sum(int(digit) for digit in str(abs(n)))
            if value < minimum:
                minimum=value

        return minimum