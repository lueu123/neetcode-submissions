class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        for n in nums:
            counts[n]+=1
        return list(sorted(counts,reverse=True,key=counts.get))[:k]
                