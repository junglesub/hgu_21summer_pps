n, init = [int(s) for s in input().split()]
gg, gb, bg, bb = [float(s) for s in input().split()]

# 1일차는 그냥 계산
good = gg if init == 0 else bg
bad = gb if init == 0 else bb

for i in range(2, n + 1):
  g = good
  b = bad
  good = g * gg + b * bg
  bad = b * bb + g * gb

print(int(good * 1000), int(bad * 1000))