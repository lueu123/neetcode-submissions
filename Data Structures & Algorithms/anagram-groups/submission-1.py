class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = collections.defaultdict(list)
        for s in strs:
            gg = ''.join(sorted(s))
            grps[gg].append(s)
        return list(grps.values())
                