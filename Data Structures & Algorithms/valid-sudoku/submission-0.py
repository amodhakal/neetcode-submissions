class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
        
        def valid_cols(col: int):
            foundset = set()
            for row in board:
                val = row[col]
                if val == ".":
                    continue

                if val in foundset:
                    return False

                foundset.add(val)

            return True

        def valid_rows(row: int):
            foundset = set()
            for val in board[row]:
                if val == ".":
                    continue

                if val in foundset:
                    return False

                foundset.add(val)

            return True

        def square(row: int, col: int):
            foundset = set()
            direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in direction:
                newrow, newcol = row + dx, col + dy
                val = board[newrow][newcol]
                if val == ".":
                    continue

                if val in foundset:
                    return False

                foundset.add(val)

            return True

        for i in range(0, len(board[0])):
            result = result and valid_cols(i)

        for i in range(0, len(board)):
            result = result and valid_rows(i)

        result = result and square(1, 1) and square(1, 4) and square(1, 7)
        result = result and square(4, 1) and square(4, 4) and square(4, 7)
        result = result and square(7, 1) and square (7, 4) and square (7, 7)

        return result