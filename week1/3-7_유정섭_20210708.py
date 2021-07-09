from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billchange = dict(zip([5, 10, 20], [0] * 3))
        for b in bills:
          billchange[b] += 1
          change = b - 5
          while change >= 10 and billchange[10] > 0:
            change -= 10
            billchange[10] -= 1
          while change >= 5 and billchange[5] > 0:
            change -= 5
            billchange[5] -= 1
          if change != 0: return False
        return True

          

t1 = Solution.lemonadeChange(None, [5, 5, 5, 10, 20])
print(t1) # True.
t2 = Solution.lemonadeChange(None, [5,5,5,5,20,20,5,5,20,5])
print(t2) # True.

'''
if b == 20:
            if bills[10] >= 1 and bills[5] >= 1:
              bills[10] -= 1
              bills[5] -= 1
            elif bills[5] >= 3:
              bills[5] -= 3
            else:
              return False
          if
'''