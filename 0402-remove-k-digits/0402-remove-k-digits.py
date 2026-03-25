class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return '0'
        stack=[]
        for val in num:
            int_val=int(val)
            while stack and stack[-1]>int_val and k>0:
                stack.pop()
                k-=1
            stack.append(int_val)
        while k > 0:
            stack.pop()
            k -= 1
        result = ''.join(map(str, stack))
        result = result.lstrip('0')
        return result if result else "0"