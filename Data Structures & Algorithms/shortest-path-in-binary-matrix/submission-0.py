class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] != 0:
            return -1 
        
        ROWS = len(grid)
        COLS = len(grid[0])

        q = collections.deque()
        visited = set((0,0))
        dirrections = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1,), (-1, -1)]
        q.append((0, 0, 1))

        while q: 
            row, col, path = q.popleft()
            if (row, col) == (ROWS -1, COLS -1): 
                return path
            
            for dr, dc in dirrections: 
                nr = row + dr
                nc = col + dc 

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 1: 
                    continue
                q.append((nr, nc, path + 1))
                visited.add((nr, nc))

        return -1
