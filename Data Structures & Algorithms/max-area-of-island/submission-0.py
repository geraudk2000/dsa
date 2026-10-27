class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        maxIsland = 0 
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row<0 or col<0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == 0: 
                return 0

            visited.add((row, col))

            return 1 + dfs(row -1, col) +  dfs(row + 1, col) + dfs(row, col -1 ) + dfs(row, col + 1)

        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 1 and (row, col) not in visited: 
                    currentIsland = dfs(row, col)
                    maxIsland = max(maxIsland, currentIsland)
        return maxIsland