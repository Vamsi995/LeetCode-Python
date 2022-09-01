class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        max_area = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
        
        
        for i in range(len(matrix)-1, -1, -1):
            
            for j in range(len(matrix[0]) - 1, -1, -1):
                
                if matrix[i][j] > 0:
                    
                    r, d, diag = 0, 0, 0
                    
                    if i + 1 <= len(matrix) - 1:
                        d = matrix[i+1][j]
                    
                    if i + 1 <= len(matrix) - 1 and j + 1 <= len(matrix[0]) - 1:
                        diag = matrix[i+1][j+1]
                    
                    if j + 1 <= len(matrix[0]) - 1:
                        r = matrix[i][j+1]
                        
                    
                    
                    matrix[i][j] += min(r, d, diag)
                    max_area = max(max_area, matrix[i][j])
            
        return max_area ** 2
        
                            
        
        