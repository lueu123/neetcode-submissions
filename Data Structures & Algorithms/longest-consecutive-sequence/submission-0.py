class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best= 0
        for n in nums:
            if n-1 in nums:      
                continue
            cur = 1               
            while n+1 in nums:   
                n += 1
                cur += 1
            best = max(best, cur)
        return best