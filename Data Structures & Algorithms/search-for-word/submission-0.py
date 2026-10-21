class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        N = len(board)
        M = len(board[0])
        word_len = len(word)
        visited = [[False for j in range(M)] for i in range(N)]

        def backtrack(w_idx, r_idx, c_idx):
            if w_idx == word_len:
                return True
            
            if (r_idx<0 or r_idx==N) or (c_idx<0 or c_idx==M) or word[w_idx]!=board[r_idx][c_idx] or visited[r_idx][c_idx]==True:
                return False
            
            visited[r_idx][c_idx] = True
            res = backtrack(w_idx+1, r_idx+1, c_idx) or backtrack(w_idx+1, r_idx-1, c_idx) or backtrack(w_idx+1, r_idx, c_idx+1) or backtrack(w_idx+1, r_idx, c_idx-1)
            visited[r_idx][c_idx] = False

            if res==True:
                return True
            
            return res

        for i in range(N):
            for j in range(M):
                if word[0]==board[i][j] and backtrack(0, i, j):
                    return True
        
        return False


        