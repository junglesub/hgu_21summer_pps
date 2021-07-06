class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
      for i in range(abs(len(b) - len(a)) * 2 + 3):
        if b in (a * i) : return i
      return -1

t1 = Solution.repeatedStringMatch(None, "ba", "ab")
print(t1)

t1 = Solution.repeatedStringMatch(None, "aa", "a")
print(t1)

"""
Skretch this.
# Rule 1. b must contain cdab abcdabcd
# Rule 2. All alphabet in b must be in a
for c in b:
  if c not in a: return -1
return -1
"""