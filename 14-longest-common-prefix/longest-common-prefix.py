class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        mi = min(strs,key=lambda w: len(w),default=None)
        prefix = ""
        counter = 0
        for i in range(len(mi),0,-1):
            for s in strs:
                if s[:i] != mi[:i] :
                    prefix = ""
                    break
                else:
                  counter += 1
                  prefix = mi[:i]
                  
            if counter == len(strs) and prefix:
                break
            else:
              counter = 0
        return prefix
        

        