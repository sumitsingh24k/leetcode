class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        max_value=0
        mapping=defaultdict(int)
        while right<len(s):
            mapping[s[right]]+=1
            while (right-left+1) -max(mapping.values())>k:
                mapping[s[left]]-=1
                left+=1
            max_value=max(max_value,right-left+1)
            right+=1
        return max_value 