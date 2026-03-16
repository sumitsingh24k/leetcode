class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        sums = set()
        for r in range(rows):
            for c in range(cols):
                # single cell rhombus
                sums.add(grid[r][c])
                size = 1
                while True:
                    if r + 2*size >= rows or c - size < 0 or c + size >= cols:
                        break
                    total = 0
                    for i in range(size):
                        total += grid[r+i][c+i]
                    for i in range(size):
                        total += grid[r+size+i][c+size-i]
                    for i in range(size):
                        total += grid[r+2*size-i][c-i]
                    for i in range(size):
                        total += grid[r+size-i][c-size+i]
                    sums.add(total)
                    size += 1
        return sorted(sums, reverse=True)[:3]
