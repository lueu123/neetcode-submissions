class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lol = collections.defaultdict(int)
        lol2 = collections.defaultdict(int)
        if len(s) != len(t):
            return False
        for l in s:
            lol[l]+=1
        for j in t:
            lol2[j]+=1
        return lol == lol2 
