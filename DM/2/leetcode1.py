from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.lens = (len(grid), len(grid[0]))
        counter = 0
        for i in range(self.lens[0]):
            for j in range(self.lens[1]):
                if grid[i][j] == "1":
                    counter += 1
                    self.propagation(i, j)
        return counter

    def propagation(self, i, j):
        self.grid[i][j] = "0"
        if i < self.lens[0] - 1 and self.grid[i + 1][j] == "1":
            self.propagation(i + 1, j)
        if i > 0 and self.grid[i - 1][j] == "1":
            self.propagation(i - 1, j)
        if j < self.lens[1] - 1 and self.grid[i][j + 1] == "1":
            self.propagation(i, j + 1)
        if j > 0 and self.grid[i][j - 1] == "1":
            self.propagation(i, j - 1)


s = Solution()
print(
    s.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
    )
)
