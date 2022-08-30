class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if visited[i][j] == False and grid[i][j] == "1":
                    self.dfs(i, j, visited, grid)
                    count += 1
        
        return count
    
    
    
    def dfs(self, i, j, visited, grid):
        
        visited[i][j] = True
        
        if i-1 >= 0 and not visited[i-1][j] and grid[i-1][j] == "1":
            self.dfs(i-1, j, visited, grid)
        
        if i+1 <= len(grid) - 1 and not visited[i+1][j] and grid[i+1][j] == "1":
            self.dfs(i+1, j, visited, grid)
        
        if j - 1 >= 0 and not visited[i][j-1] and grid[i][j-1] == "1":
            self.dfs(i, j-1, visited, grid)
            
        if j + 1 <= len(grid[0]) - 1 and not visited[i][j+1] and grid[i][j+1] == "1":
            self.dfs(i, j+1, visited, grid)
        
        
        
        