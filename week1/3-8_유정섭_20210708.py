import re
class Solution:
    def countAndSay(self, n: int) -> str:
      if n <= 1:
        return str(n)
      n = Solution.countAndSay(None, n - 1)
      result = ""
      for d in re.findall(r"((\w)\2*)", n):
        result += (str(len(d[0])) + d[1])
      return result

# Test Case
t1 = Solution.countAndSay(None, 4)
print(t1)