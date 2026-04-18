class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        direction=[(0,1),(0,-1),(1,0), (-1,0)]
        heap = [(grid[0][0], 0, 0)]
        n=len(grid)
        visited=set()
        while heap:
            value,row,col=heapq.heappop(heap)
            if row==n-1 and col==n-1:
                return value 
            for dr,dc in direction:
                nr,nc=dr+row,col+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    max_value=max(value,grid[nr][nc])
                    heapq.heappush(heap,(max_value,nr,nc))
                    
        return -1