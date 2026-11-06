class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left=0
        right=0
        seen=set()
        max_val=float('-inf')
        for char in s:
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)
            right+=1
            max_val=max(max_val,len(seen))
        return max_val