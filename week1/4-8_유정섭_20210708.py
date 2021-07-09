a, b, c = [int(x) for x in input().split()]

if b >= c:
  print(-1)
else:
  print(int(a / (c-b) + 1)) # 친구 도움 받아서 풀었음..