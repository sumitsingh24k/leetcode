class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(-1,0),(1,0),(0,-1)]
        queue=deque()
        count = 0
        time = 0
        r,c=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    count+=1
        if count==0:
            return 0
        while queue:
            n=len(queue)
            for i in range(n):
                row,col=queue.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if 0<=nr<r and 0<=nc<c and  grid[nr][nc]==1:
                        grid[nr][nc]=2
                        count-=1
                        queue.append([nr,nc])
            time+=1
        return time-1 if count == 0 else -1