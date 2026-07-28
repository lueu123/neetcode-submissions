class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l,best = 0,0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            best = max(best,len(window))
        return best
