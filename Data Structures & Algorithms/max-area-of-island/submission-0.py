class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int):
            if col < 0 or col >= len(grid[0]):
                return 0
            
            if row < 0 or row >= len(grid):
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            top =  dfs(row - 1, col)
            bottom = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            return top + bottom + left + right + 1

        maxarea = 0

        for rowidx in range(len(grid)):
            row = grid[rowidx]
            for colidx in range(len(row)):
                col = row[colidx]

                if col == 0:
                    continue

                maxarea = max(maxarea, dfs(rowidx, colidx))

        return maxarea

        
        