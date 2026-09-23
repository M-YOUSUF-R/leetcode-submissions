class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref = ""
        first_p = 0
        second_p = 1
        if not s:
            return 0
        ref += s[first_p]
        out = 0
        set_chars = set(s)
        if len(set_chars) == 1:
            return 1
        while (second_p < len(s)):
            if s[second_p] not in ref:
                ref += s[second_p]
                second_p += 1
            else:
                first_p = ref.index(s[second_p]) + 1
                ref = ref[first_p:]
            out = max(len(ref),out)
        return out

