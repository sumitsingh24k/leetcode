class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        distance=[float('inf')]*n
        distance[0]=0
        graph=[[] for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        ways=[0]*n
        ways[0]=1
        heap=[(0,0)]
        modulus=10**9+7
        while heap:
            curr,node=heapq.heappop(heap)
            for neighbour,weight in graph[node]:
                val=weight+curr
                if val<distance[neighbour]:
                    distance[neighbour]=val
                    ways[neighbour]=ways[node]
                    heapq.heappush(heap,(val,neighbour))
                elif val==distance[neighbour]:
                    ways[neighbour]+=ways[node]
        return ways[n-1]%modulus