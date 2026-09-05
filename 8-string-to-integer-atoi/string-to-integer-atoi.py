import string
class Solution:
    def myAtoi(self, s: str) -> int:

        ans = 0
        sign = 1
        s = s.strip()
        if not s:
            return 0
        for i in range(len(s)):
            if i == 0 and s[i] in ['-','+']:
                if s[i] == '-':
                    sign = - 1
            elif not s[i].isdigit():
                break
            else:
                ans = ans*10 + int(s[i])
            
        ans *= sign  
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Clamp within 32-bit signed integer range
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
            
        return ans




        