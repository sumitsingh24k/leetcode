class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n=len(arr1)
        m=len(arr2)
        count=0
        for i in range(n):
            for j in range(m):
                if abs(arr1[i]-arr2[j])<=d:
                    count+=1
                    break
        return  n-count