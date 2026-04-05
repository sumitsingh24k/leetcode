class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r,c=len(board),len(board[0])
        result=[['X']*c for _ in range(r) ]
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        queue=deque()
        for i in range(r):
            for j in range(c):
                if(i==0 or i==r-1 or j==0 or j==c-1) and   board[i][j]=='O':
                    result[i][j]='O'
                    visited.add((i,j))
                    queue.append([i,j])
        while queue:
            row,col=queue.popleft()
            for dr,dc in  direction:
                nr,nc=dr+row,dc+col
                if 0<=nr<r and 0<=nc<c and board[nr][nc]=='O' and (nr,nc) not in visited:
                    result[nr][nc]='O'
                    visited.add((nr,nc))
                    queue.append([nr,nc])
        board[:]=result