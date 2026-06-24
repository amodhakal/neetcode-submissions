class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(rowidx, colidx, chidx, visit):
            # Done
            if chidx >= len(word):
                return True

            # Out of bounds
            if rowidx < 0 or rowidx >= ROWS or colidx < 0 or colidx >= COLS:
                return False
            
            # Already used
            if (rowidx, colidx) in visit:
                return False
            
            # Can't be used
            if board[rowidx][colidx] != word[chidx]:
                return False

            # Can be used
            visit.add((rowidx, colidx))

            # Try completing word
            for diffX, diffY in DIRS:
                if dfs(rowidx + diffX, colidx + diffY, chidx + 1, visit):
                    return True

            visit.remove((rowidx, colidx))
            return False

        for rowidx in range(ROWS):
            for colidx in range(COLS):
                currset = set()
                
                if dfs(rowidx, colidx, 0, currset):
                    return True

        return False

