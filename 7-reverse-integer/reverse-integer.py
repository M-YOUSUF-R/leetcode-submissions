class Solution:
    def reverse(self, x: int) -> int:
        rev_d = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            digit = x % 10
            rev_d = rev_d * 10 + digit
            x = x // 10
        
        rev_d *= sign
        print(rev_d)
        
        INT_VAL = -2**31
        MAX_VAL = 2**31 - 1

        if rev_d < INT_VAL or rev_d > MAX_VAL:
            return 0
        return rev_d

        