class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grps = collections.defaultdict(int)
        for n in nums:
            grps[n]+=1
        return sorted(grps, key=grps.get, reverse=True)[:k]