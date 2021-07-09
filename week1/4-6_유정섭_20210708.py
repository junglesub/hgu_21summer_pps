class Solution:
    def addDigits(self, num: int) -> int:
      ans = sum([int(c) for c in str(num)])
      return ans if ans < 10 else Solution.addDigits(self, ans)