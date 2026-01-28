class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        heap = [(grid[0][0], 0, 0)]
        visited=set()
        visited.add((0,0))
        depth=0
        while heap:
            curr_level,r,c=heapq.heappop(heap)
            if curr_level > depth:
                depth=curr_level
            if r==row-1 and c==col-1:
                return depth
            for dr,dc in direction:
                nr,nc=dr+r,dc+c
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(heap,(grid[nr][nc],nr,nc))