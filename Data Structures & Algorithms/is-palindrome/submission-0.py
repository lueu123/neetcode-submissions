class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(filter(str.isalnum,s.lower()))
        return c == ''.join(reversed(c))
        