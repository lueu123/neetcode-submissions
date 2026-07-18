class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            goal=target-n
            for j,k in enumerate(nums):
                if k == goal:
                    if i != j: 
                        return [i,j]