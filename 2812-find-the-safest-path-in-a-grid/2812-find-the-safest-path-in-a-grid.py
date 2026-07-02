class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        self.sf = [[-1] * n for _ in range(n)]
        q = deque()

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    self.sf[row][col] = 0  
                    q.append((row, col))   


        curr_lvl = 1
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            curr_len = len(q)
            for _ in range(curr_len):
                x, y = q.popleft()
                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and self.sf[nx][ny] == -1:
                        self.sf[nx][ny] = curr_lvl
                        q.append((nx, ny))
            curr_lvl += 1


        # print(self.sf)
        
        # the safeness factor could not be more then sf[0][0] or sf[-1][-1]
        # since we need to start from 0,0 and end at n - 1, n - 1
        # so the safeness factor will lie in this range only i.e 0 to min(sf[0][0], sf[-1][-1])
        # as the two points are fixed in path, so is there safeness values need to be in path
        
        start_sf = self.sf[0][0]
        end_sf = self.sf[-1][-1]
        best_sf = min(start_sf, end_sf)
        if best_sf == 0:
            return 0

        if self.isFeasible(best_sf):
            return best_sf

        l,r = 0, best_sf - 1
        best_mid = 0
        while l <= r: 
            mid = (l + r) // 2
            if self.isFeasible(mid):
                best_mid = mid
                l = mid + 1
            else: 
                r = mid - 1
        # best sf is the actual optimal safness factor  
        # but best_mid is the actual which lead to valid path from start to end with max_sf 
        return best_mid

    def isFeasible(self, safeness_factor):
        # if we could reach the end from the given safeness factor then it is feasible
        # and the given safeness factor could be the answer
        q = deque([(0,0)])
        n = len(self.sf)
        visited = {(0,0)}
        while q:
            x, y = q.popleft()
            
            if x == n - 1 and y == n - 1:
                return True
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) not in visited and self.sf[nx][ny] >= safeness_factor:
                        
                        visited.add((nx, ny)) 
                        q.append((nx, ny))
        return False

