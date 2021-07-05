from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 가격 차이가 많이 나는 순
        cheapest = sorted(costs, key=lambda a : -abs(a[0] - a[1]))
        # T/O 만들기
        a = []
        b = []
        # 계산
        for item in cheapest:
          if item[0] < item[1]:
            a.append(item)
          else:
            b.append(item)
        # # 비율 맞추기
        while len(a) != len(b):
          # 가장 차이가 적게나는 마지막부터 정렬 시작
          if len(a) > len(b):
            b.append(a.pop())
          else:
            a.append(b.pop())
        return sum([i[0] for i in a]) + sum([i[1] for i in b])


# Test
t1 = Solution.twoCitySchedCost(None, [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
print(t1)

t2 = Solution.twoCitySchedCost(None, [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])
print(t2)