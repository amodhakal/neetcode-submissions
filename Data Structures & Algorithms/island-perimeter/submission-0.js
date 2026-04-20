class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    islandPerimeter(grid) {
        let perimeter = 0;
        for (let height = 0; height < grid.length; height++) {
            const current = grid[height];
            for (let width = 0; width < current.length; width++) {
                perimeter += this.getPerimeter(grid, width, height);
            }
        }
        return perimeter;
    }

    getPerimeter(grid, width, height) {
        // use row-major indexing: grid[row][col] -> grid[height][width]
        if (grid[height][width] === 0) {
            return 0;
        }

        let openSides = 0;
        // left
        if (width - 1 < 0 || grid[height][width - 1] === 0) openSides++;
        // up
        if (height - 1 < 0 || grid[height - 1][width] === 0) openSides++;
        // right
        if (width + 1 >= grid[0].length || grid[height][width + 1] === 0) openSides++;
        // down
        if (height + 1 >= grid.length || grid[height + 1][width] === 0) openSides++;

        return openSides;
    }
}
