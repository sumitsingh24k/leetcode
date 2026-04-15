class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap=[(0,0,0)]
        r,c=len(heights),len(heights[0])
        grid = [[float('inf')] * c for _ in range(r)]
        grid[0][0]=0
        direction=[(0,-1),(0,1),(1,0),(-1,0)]
        while heap:
            val,row,col=heapq.heappop(heap)
            if row==r-1 and col==c-1:
                return val
            for dr,dc in direction:
                nr,nc=dr+row,dc+col
                if 0<=nr<r and 0<=nc<c:
                    cal = max(val, abs(heights[row][col] - heights[nr][nc]))
                    if grid[nr][nc]>cal:
                        grid[nr][nc]=cal
                        heapq.heappush(heap,(cal,nr,nc))
        return -1
