class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        if not s:
            return 0

        sign = 1
        res = 0

        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                sign = -1
            s = s[1:] 

        for char in s:
            if not char.isdigit():
                break
            res = res * 10 + int(char)
        res = res * sign

        if res < -2**31:
            return -2**31

        elif res > 2**31 - 1:
            return 2**31 - 1
        
        return res