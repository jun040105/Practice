#leetcode qn 74


class Solution(object):
    def exist(self, board, word):
        
        m = len(board)
        n = len(board[0])

        def dfs(y, x, i):

            if y < 0 or y >= m or x < 0 or x >= n:
                return False
            
            if board[y][x] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            temp = board[y][x]
            board[y][x] = "#"

            passed = (
                dfs(y-1, x, i+1) or
                dfs(y+1, x, i+1) or 
                dfs(y, x-1, i+1) or
                dfs(y, x+1, i+1)
            )

            board[y][x] = temp

            return passed

        for y in range(m):
            for x in range(n):
                if dfs(y, x, 0):
                    return True
        
        return False
