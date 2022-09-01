class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        unique = set()
        
        visited = set()
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    pivot = [i, j]
                    rel = []
                    self.dfs(pivot, i, j, visited, grid, unique, rel)
                    if str(rel) not in unique:
                        unique.add((str(rel)))
                    count = max(len(unique), count)
        
        # print(unique)
        return count
    
    def dfs(self, source, i, j, visited, grid, unique, rel):
        
        if (i, j) not in visited:
            visited.add((i, j))
        else:
            return
        
        direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        
        for di in direc:
            
            r = i + di[0]
            c = j + di[1]
            
            if r >=0 and c >=0 and r <= len(grid)-1 and c <= len(grid[0])-1:
                
                if (r, c) not in visited and grid[r][c] == 1:
                    
                    rel.append(di[0])
                    rel.append(di[1])
                    rel.append(abs(source[0] - r))
                    rel.append(abs(source[1] - c))
                    
                    self.dfs(source, r, c, visited, grid, unique, rel)
                    
        
        
        
        
        
        
        
        
        