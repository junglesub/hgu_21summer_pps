from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(f"The array represents the integer {''.join([str(c) for c in digits])}.")
        return [int(c) for c in str(sum(map(lambda e: e[1] * (10 **(len(digits) - e[0] - 1)), enumerate(digits))) + 1)]

t1 = Solution.plusOne(None, [1, 2, 3])
print(t1)