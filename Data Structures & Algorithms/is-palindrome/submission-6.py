class Solution:
    def isPalindrome(self, s: str) -> bool:
        lol = []
        for char in s.lower():
            if char.isalnum():
                lol.append(char)
        return lol == lol[::-1]