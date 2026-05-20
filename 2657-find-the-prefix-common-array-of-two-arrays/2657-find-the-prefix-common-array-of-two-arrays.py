class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        count=0
        result=[]
        seen=set()
        for i in range(n):
            if A[i] in seen:
                count+=1
            seen.add(A[i])
            if B[i] in seen:
                count+=1
            seen.add(B[i])
            result.append(count)
        return result