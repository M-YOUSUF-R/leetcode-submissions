import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = string.ascii_letters + string.digits
        new_s = ""
        for i in s:
            if i in alphabet:
                new_s += i.lower()
        rev_new_s = new_s[::-1]

        if new_s == rev_new_s:
            return True
        return False

        
        