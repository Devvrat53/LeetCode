class Solution:
    # Gaurav Saini
    def __init__(self):
        self.done = set()
        self.deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    def safe(self, r: int, c: int, grid):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] != '0'

    def dfs(self, r, c, grid):
        if (r, c, ) in self.done:
            return
        self.done.add((r, c, ))
        for delta in self.deltas:
            new_r = r + delta[0]
            new_c = c + delta[1]
            if self.safe(new_r, new_c, grid) and (new_r, new_c, ) not in self.done:
                self.dfs(new_r, new_c, grid)

    def numIslands(self, grid) -> int:
        self.done = set()
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.safe(r, c, grid) and (r, c, ) not in self.done:
                    self.dfs(r, c, grid)
                    ans += 1
        return ans


class Solution1:
    # https://www.youtube.com/watch?v=gCswsDauXPc
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands


if __name__ == '__main__':
    soln = Solution()
    soln1 = Solution1()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(soln.numIslands(grid))