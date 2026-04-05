class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        queue=deque([])
        visited=[-1]*n
        for i in range(n):
            if visited[i]==-1:
                visited[i]=0
                queue.append(i)
                while queue:
                    node=queue.popleft()
                    for neighbour in graph[node]:
                        if visited[neighbour]==-1:
                            visited[neighbour]=1+visited[node]
                            queue.append(neighbour)
                        elif visited[neighbour]==visited[node]:
                            return False 
        return True