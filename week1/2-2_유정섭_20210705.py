import re

result = []

n = int(input())
for _ in range(n):
  firstN = lambda n: n * (n+1) / 2
  result.append(sum([firstN(len(i)) for i in re.compile("(O+)").findall(input())]))

for res in result:
  print(int(res))