from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      prefix = ""
      for i in range(min([len(s) for s in strs])):
        pc = strs[0][i]
        for word in strs[1:]:
          if word[i] != pc: return prefix
        prefix += pc
      return prefix
      
print(Solution.longestCommonPrefix(None, ["dog","racecar","car"]))
