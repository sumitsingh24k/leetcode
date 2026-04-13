from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph=defaultdict(list)
        indegree=[0]*len(graph)
        result=[]
        n = len(graph)
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                indegree[u]+=1
        queue = deque([i for i in range(n) if indegree[i] == 0]) 
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            node=queue.popleft()
            result.append(node)
            for neighbour in reverse_graph[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        return sorted(result)