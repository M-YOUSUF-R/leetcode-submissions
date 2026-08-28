class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = dict.fromkeys(s,0)
        dic2 = dict.fromkeys(t,0)
        for i in s:
            dic1[i] += 1
        
        for  i in t:
            dic2[i] += 1

        return dic1 == dic2

