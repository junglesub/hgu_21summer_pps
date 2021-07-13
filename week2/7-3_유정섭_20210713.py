from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)/2
        cnt = {}
        for x in nums:
          if x not in cnt: cnt[x] = 0
          cnt[x] += 1
          if cnt[x] > maj: return x