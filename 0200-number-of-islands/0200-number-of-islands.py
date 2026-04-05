class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        r,c=len(grid),len(grid[0])
        def dfs(row,col):
            if row<0 or row>=r or col<0 or col>=c:
                return
            if grid[row][col]=='0':
                return 
            if grid[row][col]=='1':
                grid[row][col]='0'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count    