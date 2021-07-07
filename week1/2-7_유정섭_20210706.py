from typing import List
def backspaceStr(s):
  bk = 0
  result = ""
  for c in s[::-1]:
    if c == "#": bk += 1
    elif bk > 0: bk -= 1
    else: result = c + result
  return result
class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    return backspaceStr(s) == backspaceStr(t)

# Test case
t1 = Solution.backspaceCompare(None, "ab#c", "ad#c")
print(t1)