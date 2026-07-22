class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = collections.defaultdict(list)
        for s in strs:
            team = ''.join(sorted(s))
            grps[team].append(s)
        return list(grps.values())

        
        