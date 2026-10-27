class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] != 0 or grid[ROWS - 1][COLS - 1] !=0:
            return -1 
        
        q = collections.deque()
        q.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while q: 
            r, c, path = q.popleft()
            if (r, c) == (ROWS-1, COLS -1): 
                return path
            
            for dr, dc in directions: 
                row = r + dr
                col = c + dc 

                if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == 1: 
                    continue
                q.append((row, col, path+1))
                visited.add((row, col))
        return -1 
            






