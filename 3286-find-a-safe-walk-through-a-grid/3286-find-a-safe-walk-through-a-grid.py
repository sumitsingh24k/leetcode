from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        row,col=len(grid),len(grid[0])
        if grid[0][0] == 1:
            health -= 1
        if health < 1:
            return False
        queue = deque([(0, 0, health)])
        visited=set()
        visited.add((0,0,health))
        while queue:
            r,c,health=queue.popleft()
            if r==row-1 and c==col-1 and health>=1:
                return True
            for dr,dc in direction:
                nr,nc=dr+r,dc+c
                if 0<=nr<row and 0<=nc<col:
                    if grid[nr][nc]==1:
                        curr_health=health-1
                        if curr_health>=1 and (nr, nc, curr_health) not in visited:
                            visited.add((nr,nc,curr_health))
                            queue.append([nr,nc,curr_health])
                    if grid[nr][nc]==0 and  (nr, nc, health) not in visited:
                        visited.add((nr,nc,health))
                        queue.append([nr,nc,health])
        return False
            