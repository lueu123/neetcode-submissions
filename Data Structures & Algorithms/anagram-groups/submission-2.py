class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = collections.defaultdict(list)
        for s in strs:
            g = ''.join(sorted(s))
            grps[g].append(s)
        return list(grps.values())