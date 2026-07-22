class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for l in s:
            if l.isalnum():
                clean+=l.lower()
        p1,p2 = 0,len(clean)-1  
        while p1 < p2:
            if clean[p1] != clean[p2]:
                return False
            p1+=1
            p2-=1
        return True