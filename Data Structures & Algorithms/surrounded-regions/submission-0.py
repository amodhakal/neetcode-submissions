class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        not_surrounded = set()

        def dfs(row, col):
            if row < 0 or row >= ROWS:
                return
            
            if col < 0 or col >= COLS:
                return

            if board[row][col] == "X":
                return
            
            if (row, col) in not_surrounded:
                return

            not_surrounded.add((row, col))
            DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in DIRS:
                dfs(row + dx, col + dy)

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        print(not_surrounded)

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in not_surrounded:
                    continue
                
                board[row][col] = "X"
