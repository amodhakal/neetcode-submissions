class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [ (0, -1), (0, 1), (-1, 0), (1, 0)]
        q = collections.deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()
            dist = grid[row][col]

            for dx, dy in DIRS:
                row2, col2 = row + dx, col + dy
                if row2 < 0 or row2 >= ROWS:
                    continue
                if col2 < 0 or col2 >= COLS:
                    continue
                if grid[row2][col2] != 2147483647:
                    continue

                grid[row2][col2] = dist + 1
                q.append((row2, col2))
                



