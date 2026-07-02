class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1:
            health -= 1
        if health < 1:
            return False
        queue = deque([(0, 0, health)])
        visited = set()
        visited.add((0, 0, health))
        while queue:
            r, c, health = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        curr_health = health - 1
                        if curr_health >= 1 and (nr, nc, curr_health) not in visited:
                            visited.add((nr, nc, curr_health))
                            queue.append((nr, nc, curr_health))
                    else:
                        if (nr, nc, health) not in visited:
                            visited.add((nr, nc, health))
                            queue.append((nr, nc, health))
        return False