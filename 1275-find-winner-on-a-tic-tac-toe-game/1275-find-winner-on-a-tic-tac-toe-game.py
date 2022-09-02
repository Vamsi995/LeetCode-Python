class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        swtch = 0
        
        row = [0, 0, 0]
        col = [0, 0, 0]
        diag = 0
        anti_diag = 0
        
        for i in range(len(moves)):
            
            if swtch == 0:
                row[moves[i][0]] += 1
                col[moves[i][1]] += 1
                if moves[i][0] == moves[i][1]:
                    diag += 1
                
                if moves[i][0] == 2 - moves[i][1]:
                    anti_diag += 1
                    
                swtch = 1
                
                
                if row[moves[i][0]] == 3 or col[moves[i][1]] == 3 or diag == 3 or anti_diag == 3:
                    return "A"
                    
            else:
                row[moves[i][0]] -= 1
                col[moves[i][1]] -= 1
                if moves[i][0] == moves[i][1]:
                    diag -= 1
                
                if moves[i][0] == 2 - moves[i][1]:
                    anti_diag -= 1
                
                swtch = 0
                
                
                if row[moves[i][0]] == -3 or col[moves[i][1]] == -3 or diag == -3 or anti_diag == -3:
                    return "B"
            
            
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"

        
        
        