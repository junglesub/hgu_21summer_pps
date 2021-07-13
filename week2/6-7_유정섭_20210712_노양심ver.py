class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 무식한 방법
        word = s
        chs = list(word)

        removed = True
        while removed:
          removed = False
          for c in chs:
            rem = c * 2 # c -> cc
            if rem in word:
              removed = True
              word = word.replace(rem, "")
        return word
        
# TC
t1 = Solution.removeDuplicates(None, "abbaca")
print(t1)
t1 = Solution.removeDuplicates(None, "azxxzy")
print(t1)
    