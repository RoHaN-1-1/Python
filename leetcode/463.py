class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land = 0
        big_peri = 0
        for i in range(0,len(grid),1):
            for j in range(0,len(grid[0]),1):
                if grid[i][j] == 1:
                    big_peri += 4
                    if i > 0 and grid[i-1][j] == 1:
                        big_peri -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        big_peri -= 2
        return big_peri