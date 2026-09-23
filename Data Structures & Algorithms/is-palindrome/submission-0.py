class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(str.isalnum , s))
        if s1.lower() == s1[::-1].lower():
            return True

        return False
        