class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     res = []
     nums.sort()
     for i, n in enumerate(nums):
        diff = -n
        l, r = i+1, len(nums) - 1
        while l<r:
            s = nums[l] + nums[r]
            if s == diff:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif s < diff:
                l += 1
            else:
                r -= 1
    
     return list(set( tuple(x) for x in res))