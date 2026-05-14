class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      longest = 0
      s = set(nums)
      for x in s:
        if x - 1 not in s:
          streak = 0
          curr = x
          while curr in s:
            streak += 1
            curr += 1
          longest = max(longest, streak)
      return longest
          
  


            