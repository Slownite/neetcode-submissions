class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = []
        nums.sort()
        for i, n in enumerate(nums):
            l, r = i+1, len(nums) - 1
            target = -n
            while l < r:
                s = nums[l] + nums[r]
                if  s == target:
                    seen.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return list(set(tuple(x) for x in seen))
