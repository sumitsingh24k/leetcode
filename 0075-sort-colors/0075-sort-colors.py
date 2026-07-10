class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = Counter(nums)
        index = 0

        for color in [0, 1, 2]:
            for _ in range(freq[color]):
                nums[index] = color
                index += 1