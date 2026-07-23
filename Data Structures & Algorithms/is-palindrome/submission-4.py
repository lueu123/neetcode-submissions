class Solution:
    def isPalindrome(self, s: str) -> bool: 
        c = ''
        for l in s:
            if l.isalnum():
                c += l.lower()
        
        p1,p2 = 0,len(c)-1

        while p1 < p2:
            if c[p1] == c[p2]:
                p1+=1
                p2-=1
            else:
                return False
        return True