class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = dict()
        # Store all visited
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                visited[(row, col)] = False

        # DFS entire island and claim the lands
        # raise Exception if gotten to a land 
        # already claimed which should never happen
        def dfs_island(row, col):
            # Visited already
            if visited[(row, col)]:
                return

            # Set to visited
            visited[(row, col)] = True

            # Ignore water
            if grid[row][col] == '0':
                return

            top = (row - 1, col)
            bottom = (row + 1, col)
            left = (row, col - 1)
            right = (row, col + 1)

            if row > 0 and not visited[top]:
                dfs_island(top[0], top[1])

            if col > 0 and not visited[left]:
                dfs_island(left[0], left[1])

            if row < len(grid) - 1 and not visited[bottom]:
                dfs_island(bottom[0], bottom[1])

            if col < len(grid[0]) - 1 and not visited[right]:
                dfs_island(right[0], right[1])

        # Go through each row, col 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Do not do visited 
                if visited[(row, col)]:
                    continue

                # Continue if water
                if grid[row][col] == '0':
                    continue

                # Found a new landmass so add 1
                islands += 1

                # DFS island
                dfs_island(row, col)

                # Set current to visited
                visited[(row, col)] = True

                print(visited)

        return islands
        