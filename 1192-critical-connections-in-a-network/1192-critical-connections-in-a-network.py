class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for (u,v ) in connections:
            graph[u].append(v)
            graph[v].append(u)
        timer=0
        bridge=[]
        visited=set()
        time_insertion=[-1]*n
        low=[-1]*n
        def dfs( node,parent):
            nonlocal timer
            visited.add(node)
            low[node]=timer
            time_insertion[node]=timer
            timer+=1
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if neighbour not in visited:
                    dfs(neighbour,node)
                    low[node]=min(low[node],low[neighbour])
                    if low[neighbour]>time_insertion[node]:
                        bridge.append([node,neighbour])
                else:
                    low[node]=min(low[node],time_insertion[neighbour])
        for i in range(n):
            if i not in visited:

                dfs(i,-1)
        return bridge