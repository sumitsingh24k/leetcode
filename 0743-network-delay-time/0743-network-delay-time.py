class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        heap=[(0,k)]
        distance=[float('inf')]*(n+1)
        distance[k]=0
        heapq.heapify(heap)
        while heap:
            dist,node=heapq.heappop(heap)
            for neighbour,val in graph[node]:
                value=dist+val
                if value<distance[neighbour]:
                    distance[neighbour]=value
                    heapq.heappush(heap,(value,neighbour))
        max_val=max(distance[1:])
        return max_val if max_val != float('inf') else -1