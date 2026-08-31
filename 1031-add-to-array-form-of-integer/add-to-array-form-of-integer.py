class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num) -1  
        number = 0
        for i in num:
            number += i*(10**n)
            n -= 1
        out_num = number + k
        
        res = []
        while out_num:
            d = out_num % 10
            res.append(d)
            out_num = out_num // 10
        return res[::-1]


        