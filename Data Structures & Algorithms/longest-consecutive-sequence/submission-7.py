class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      longest = 0
      s = set(nums)
      for x in s:
        if x - 1 not in s:
          streak = 1
          curr = x
          while curr + 1 in s:
            curr += 1
            streak += 1
          longest = max(streak, longest)
      return longest



            