class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for x in s:
            if x - 1 not in s:
                curr = x
                streak = 1
                while curr +1 in s:
                    streak += 1
                    curr += 1
                longest = max(streak, longest)
        return longest
  


            