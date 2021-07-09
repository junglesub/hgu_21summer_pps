import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
      if n <= 0: return False
      return math.log(n, 4).is_integer()
        # return (n ** 0.25).is_integer()

print(Solution.isPowerOfFour(None, 1))