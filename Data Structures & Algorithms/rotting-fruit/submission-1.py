class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        days = 0
        fresh = 0
        q = collections.deque()
        visited = set()
        # searching for rotten fruit
        for row in range(ROWS): 
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
                if grid[row][col] == 1: 
                    fresh += 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row<0 or col<0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == 2 or grid[row][col] == 0:
                        continue
                    fresh -= 1
                    q.append((row, col))
                    visited.add((row, col))
            days += 1
        return days if fresh == 0 else -1

        


         
        

