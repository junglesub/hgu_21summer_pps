# 사실 정석대로 풀려면 dictionary 을 사용해야하지만 귀찮기에...

table = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time = 0
for c in input():
  time += 3 + next(i for i, x in enumerate(table) if c in x)
print(time)