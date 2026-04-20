class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  # size of each component

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        # merge smaller into bigger
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]


class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n * n)

        # helper to convert 2D to 1D index
        def index(x, y):
            return x * n + y

        # directions: up, down, left, right
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        # Step 1: Union all connected 1's
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            dsu.union(index(i,j), index(ni,nj))

        # Step 2: Track size of each root component
        root_area = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    r = dsu.find(index(i,j))
                    root_area[r] = dsu.size[r]

        max_area = max(root_area.values(), default=0)  # handle all 0's grid

        # Step 3: For each 0, see which unique islands we can connect
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    area = 1  # flip this 0 to 1
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            r = dsu.find(index(ni,nj))
                            if r not in seen:
                                seen.add(r)
                                area += dsu.size[r]
                    max_area = max(max_area, area)

        return max_area
