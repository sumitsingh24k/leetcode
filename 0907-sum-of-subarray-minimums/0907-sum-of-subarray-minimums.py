class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        prev_small = [0] * n
        next_small = [0] * n
        stack1=[]
        val=0
        for i in range(n-1, -1, -1):
            while stack1 and arr[stack1[-1]] > arr[i]:
                stack1.pop()
            if not stack1:
                next_small[i] = n
            else:
                next_small[i] = stack1[-1]
    
            stack1.append(i)
        stack2=[]
        for i in range(n):
            while stack2 and arr[stack2[-1]] >= arr[i]:
                stack2.pop()
            if not stack2:
                prev_small[i] = -1
            else:
                prev_small[i] = stack2[-1]
            stack2.append(i)
        for i in range(n):
            left=i-prev_small[i]
            right=next_small[i]-i
            val+=arr[i]*left*right
        return val % (10**9+7) 