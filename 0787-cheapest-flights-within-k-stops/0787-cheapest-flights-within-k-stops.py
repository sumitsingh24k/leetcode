class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        queue=deque([(0,src,0)])
        distance=[float('inf')]*n
        distance[src]=0
        graph=[[] for _ in range(n)]
        for u,v,weight in flights:
            graph[u].append((v,weight))
        while queue:
            curr_weight,source,steps=queue.popleft()
            if steps>k:
                continue
            for neighbour,weight in graph[source]:
                val=curr_weight+weight
                if distance[neighbour] > val:
                    distance[neighbour]=val
                    queue.append((val,neighbour,steps+1))
        return -1 if distance[dst] == float('inf') else distance[dst]