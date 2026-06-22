class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pconnect = set()
        aconnect = set()
        result = []

        COL, ROW = len(heights[0]), len(heights)
        dirChange = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(rowidx, colidx, prevheight, currset):
            # Return if this has been connected already
            if (rowidx, colidx) in currset:
                return

            # Return if out of bounds
            if rowidx < 0 or colidx < 0 or rowidx >= ROW or colidx >= COL:
                return

            # Determine if prevheight was lower than current
            # If true, water can't go further so stop
            currheight = heights[rowidx][colidx]
            if currheight < prevheight:
                return

            # Can reach
            currset.add((rowidx, colidx))

            # Try the four other directions
            for dirX, dirY in dirChange:
                newX, newY = dirX + rowidx, dirY + colidx
                dfs(newX, newY, currheight, currset)

        for i in range(ROW):
            dfs(i, 0, 0, pconnect)

        for i in range(ROW):
            dfs(i, COL - 1, 0, aconnect)

        for i in range(COL):
            dfs(0, i, 0, pconnect)

        for i in range(COL):
            dfs(ROW - 1, i, 0, aconnect)

        for rowidx in range(ROW):
            for colidx in range(COL):
                value = (rowidx, colidx)
                if value in pconnect and value in aconnect:
                    result.append([rowidx, colidx])
        return result
