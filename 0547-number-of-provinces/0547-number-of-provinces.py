class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        count=0
        def dfs(start):
            for neighbour in range(n):
                if isConnected[start][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour]=True
                    dfs(neighbour)
        for i in range(n):
            if not visited[i]:
                visited[i]=True
                dfs(i)
                count+=1
        return count 