class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        length = 0
        for char in s:
            if char not in char_set:
                char_set.add(char) 
            else:
                length += 2 # we've got a pair , so it can increase the palindrome length
                char_set.remove(char) # let's remove them so new pair can found
        if char_set: # there is left only 1 time comming values , so it can increase the length only for once
            length += 1
        return length