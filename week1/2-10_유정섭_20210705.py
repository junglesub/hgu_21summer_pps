class Solution:
    def convert(self, s: str, numRows: int) -> str:
      if numRows == 1: return s
      row_wo = [""] * numRows

      climb = False
      row = 0

      for c in s:
        row_wo[row] += c
        if not climb:
          row += 1
          if row >= numRows:
            climb = True
            row -= 2
        else:
          row -= 1
          if row <= 0:
            climb = False
      return "".join(row_wo)

# Test case
t1 = Solution.convert(None, "PAYPALISHIRING", 2)
print(t1)

# # Print solution
# print("".join(row_wo))

"""
기존 생각 -> 생각해보니 col 정보가 필요 없음.
# 공식이나 패턴이 있지 않을까?
word = "PAYPALISHIRING"
numRows = 4
row_wo = [""] * numRows

climb = False
row = 0
col = 0

print(row_wo)
for c in word:
  row_wo[row] += c
  print(row, col, c)
  if not climb:
    row += 1
    if row >= numRows:
      climb = True
      row -= 2
      col += 1
  else:
    row -= 1
    col += 1
    if row <= 0:
      climb = False
"""