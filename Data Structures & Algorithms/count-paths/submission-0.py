class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initial
        dp = [ [0] * (n - 1) + [1]] * (m - 1) + [[1] * n]
        print(dp)

        # 2d DP
        for rowidx in range(m - 2, -1, -1):
            for colidx in range(n - 2, -1, -1):
                dp[rowidx][colidx] = dp[rowidx + 1][colidx] + dp[rowidx][colidx + 1]

        return dp[0][0]
        