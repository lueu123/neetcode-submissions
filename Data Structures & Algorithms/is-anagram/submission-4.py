class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for l in s:
            if l not in count_s:
                count_s[l]=0
            count_s[l]+=1
        for l in t:
            if l not in count_t:
                count_t[l]=0
            count_t[l]+=1
        return count_s == count_t