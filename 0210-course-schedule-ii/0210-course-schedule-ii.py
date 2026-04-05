class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        result=[]
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        queue=deque([i for i in range(numCourses) if indegree[i]==0])
        while queue:
            node=queue.popleft()
            result.append(node)
            for neighbour in graph[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        if len(result)==numCourses :
            return result
        else:
            return []