class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        n=len(isConnected)
        visited=[0]*n
        def dfs(start):
            for neighbour in range(n):
                if isConnected[start][neighbour]==1 and not visited[neighbour]:
                    visited[neighbour]=1
                    dfs(neighbour)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                visited[i]=True
                count+=1
        return count