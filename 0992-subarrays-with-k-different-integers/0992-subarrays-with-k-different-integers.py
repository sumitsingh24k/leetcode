class Solution:
    def at_most(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        total = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) > k: 
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            total += (right - left + 1)

        return total  
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k - 1)
