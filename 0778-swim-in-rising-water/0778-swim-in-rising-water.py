class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited=set()
        heap = [(grid[0][0], 0, 0)]
        len_row,len_col=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        while heap:
            val,row,col=heapq.heappop(heap)
            if row == len_row - 1 and col == len_col - 1:
                return val
            for dr,dc in directions:
                nr,nc=dr+row,dc+col
                if 0<=nr<len_row and 0<=nc<len_col:
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        max_val=max(val,grid[nr][nc])
                        heapq.heappush(heap,(max_val,nr,nc))
        return -1 