class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
            
        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [""] * numRows
        currRow = 0
        direction = 1  # 1 means going down, -1 means going up
    
        for char in s:
            rows[currRow] += char
    
            # Change direction at the top or bottom
            if currRow == 0:
                direction = 1
            elif currRow == numRows - 1:
                direction = -1
    
            currRow += direction
    
        return "".join(rows)
    