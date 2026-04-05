class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r,c=len(mat),len(mat[0])
        result=[[0]*c for _ in range(r)]
        queue=deque()
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    queue.append([i,j,0])
                    visited.add((i,j))
        while queue:
            row,col,distance=queue.popleft()
            for dr,dc in direction:
                nr,nc=dr+row,dc+col
                if 0<=nr<r and 0<=nc<c and (nr,nc) not in visited:
                    result[nr][nc]=1+distance
                    visited.add((nr, nc))
                    queue.append([nr,nc,1+distance])
        return result 