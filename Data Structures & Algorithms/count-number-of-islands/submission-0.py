class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()

        def dfs(row, col): 
            if row<0 or col<0 or row == ROWS or col == COLS or grid[row][col] == "0" or (row, col) in visited:
                return 
            
            visited.add((row, col))
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            for dr, dc in directions: 
                nr = row + dr
                nc = col + dc 
                dfs(nr, nc)
        
        for row in range(ROWS):
            for col in range(COLS): 
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1
        
        return islands
