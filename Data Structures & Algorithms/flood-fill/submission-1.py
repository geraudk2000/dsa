class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        ROWS = len(image)
        COLS = len(image[0])

        q = collections.deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))
        original_color = image[sr][sc]
        while q: 
            r, c = q.popleft()

            image[r][c] = color

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions: 
                row = r + dr
                col = c + dc 

                if row<0 or col<0 or row == ROWS or col == COLS or (row, col) in visited or image[row][col] != original_color:
                    continue
                q.append((row, col))
                visited.add((row, col))
        return image

