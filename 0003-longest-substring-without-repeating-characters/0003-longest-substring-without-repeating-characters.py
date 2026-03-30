class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        seen=set()
        max_value=float('-inf')
        if len(s)==0:
            return 0
        for char in s:
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)
            right+=1
            max_value=max(max_value,len(seen))
        return max_value 
 