class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count=0
        r,c=len(grid),len(grid[0])
        queue=deque()
        visited=set()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    count+=1
                if (i==0 or j==0 or i==r-1 or j==c-1) and grid[i][j]==1:
                    queue.append([i,j])
                    visited.add((i,j))
                    count -= 1   
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            row,col=queue.popleft()
            for dr,dc in direction:
                nr,nc=dr+row,dc+col
                if 0<=nr<r and 0<=nc<c and (nr,nc) not in visited:
                    if grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        count-=1
                        queue.append([nr,nc])
        return count 