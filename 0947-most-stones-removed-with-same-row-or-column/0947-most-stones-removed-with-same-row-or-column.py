class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = max(x for x, y in stones)
        max_col=max(y for x,y in stones)
        edges=[]
        size = max_row + max_col + 2   
        for (x, y) in stones:
            edges.append([x, y + max_row + 1])
        parent = [i for i in range(size)]
        rank=[0]*size
        def find(x):
            if parent[x]!=x:
                 parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            root_x=find(x)
            root_y=find(y)
            if root_x==root_y:
                return 
            if rank[root_x]>rank[root_y]:
                parent[root_y]=root_x
            elif rank[root_x]<rank[root_y]:
                parent[root_x]=root_y
            else:
                parent[root_y]=root_x
                rank[root_x]+=1
        for x,y in edges:
            union(x,y)
        seen = set()
        for x, y in edges:
            seen.add(find(x))
            seen.add(find(y))
            components = len(seen)
        return len(stones) - components
