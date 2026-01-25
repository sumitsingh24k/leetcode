class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        graph_weight=[[float('inf')]*col for _ in range(row)]
        directions=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        visited=set()
        graph_weight[0][0]=1
        if grid[0][0]==1:
            return -1
        queue = deque([(0, 0)])
        visited.add((0, 0))
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr,nc=dr+r,c+dc
                if 0<=nr<row and 0<=nc<col and  (nr,nc) not in visited:
                    if grid[nr][nc]==0:
                        val=graph_weight[r][c]+1
                        if graph_weight[nr][nc]>val:
                            graph_weight[nr][nc]=val
                        visited.add((nr,nc))
                        queue.append((nr, nc))
        if graph_weight[row-1][col-1]!=float('inf'):
            return graph_weight[row-1][col-1]
        else:
            return -1