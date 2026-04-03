class Solution(object):
    def isValidSudoku(self, board):
        # 1. Check Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item != '.' : # Fixed syntax here
                    if item in s: return False
                    s.add(item)

        # 2. Check Columns
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item != '.':
                    if item in s: return False
                    s.add(item)

        # 3. Check 3x3 Boxes
        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i, j in starts:
            s = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item != '.':
                        if item in s: return False
                        s.add(item)
        
        return True