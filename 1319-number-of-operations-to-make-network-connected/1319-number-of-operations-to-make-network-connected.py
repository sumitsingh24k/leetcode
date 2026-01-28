class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        rank=[0]*n
        parent=[i for i in range(n)]
        component=0
        count=0
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            nonlocal count 
            x_value=find(x)
            y_value=find(y)
            if x_value==y_value:
                count+=1
                return 
            if rank[x_value]>rank[y_value]:
                parent[y_value]=x_value
            elif rank[y_value]>rank[x_value]:
                parent[x_value]=y_value
            elif rank[x_value]==rank[y_value]:
                rank[x_value]+=1
                parent[y_value]=x_value
        for u,v in connections:
            union(u,v)
        for i in range(n):
            if find(i) == i:
                component+=1
        return component - 1 if count >= component - 1 else -1
 