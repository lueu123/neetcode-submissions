from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   # {1: 1, 2: 2, 3: 3}
        return sorted(count, key=lambda n: count[n], reverse=True)[:k]