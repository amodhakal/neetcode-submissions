class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if row < 0 or row >= ROWS:
                return
            
            if col < 0 or col >= COLS:
                return

            if board[row][col] == "X":
                return
            
            if board[row][col] == "T":
                return

            board[row][col] = "T"
            for dx, dy in DIRS:
                dfs(row + dx, col + dy)

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"


