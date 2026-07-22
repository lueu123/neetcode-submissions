class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #cant have duplicate triplets so shuld use a set() to store the teams
        nums = sorted(nums)
        grps = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                k = nums[i]+nums[j]
                if k < 0:
                    k = abs(k)
                else:
                    k = -k
                if k in nums[j+1:]:
                    grps.add((k,nums[i],nums[j]))
                
        return list(grps)