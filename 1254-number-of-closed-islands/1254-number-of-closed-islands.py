class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        len_row,len_col=len(grid),len(grid[0])
        queue=deque()
        visited=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len_row):
            for j in range(len_col):
                if (i==0 or j==0 or i==len_row-1 or j==len_col-1) and grid[i][j]==0:
                    queue.append([i,j])
                    grid[i][j] = 1
        while queue:
            row,col=queue.popleft()
            for dr,dc in directions:
                new_row,new_col=dr+row,dc+col
                if  0<=new_row<len_row and  0<=new_col<len_col:
                    if grid[new_row][new_col]==0:
                        grid[new_row][new_col]=1
                        queue.append([new_row,new_col]) 
        count=0
        def dfs(curr_row,curr_col):
            if curr_row < 0 or curr_row >= len_row or curr_col < 0 or curr_col >= len_col:
                return
            if grid[curr_row][curr_col]==1:
                return
            grid[curr_row][curr_col] = 1 
            dfs(curr_row-1,curr_col)
            dfs(curr_row+1,curr_col)
            dfs(curr_row,curr_col-1)
            dfs(curr_row,curr_col+1)
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 0:   
                    dfs(i, j)
                    count += 1
        return count