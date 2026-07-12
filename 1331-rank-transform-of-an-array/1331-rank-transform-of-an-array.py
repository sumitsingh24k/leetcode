class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_dict = {}
        rank=1
        for num in sorted_unique:
            rank_dict[num] = rank
            rank += 1

        return [rank_dict[num] for num in arr]