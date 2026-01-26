class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance=[float('inf')]*n
        graph=[[] for _ in range(n)]
        for u,v,weight in flights:
            graph[u].append((v,weight))
        distance[src]=0
        queue=deque([(0,src,0)])
        while queue:
            curr_weight,node,steps=queue.popleft()
            if steps>k:
                continue  
            for neighbour,weight in graph[node]:
                val=curr_weight+weight
                if val < distance[neighbour]:
                    distance[neighbour]=val
                    queue.append((val,neighbour,steps+1))
        if distance[dst]==float('inf'):
            return -1
        return distance[dst]