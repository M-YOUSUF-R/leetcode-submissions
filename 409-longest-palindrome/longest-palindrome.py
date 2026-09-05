class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        length = 0
        for char in s:
            if char not in char_set:
                char_set.add(char)
            else:
                length += 2
                char_set.remove(char)
        if char_set:
            length += 1
        return length