n, k = [int(x) for x in input().split()]

ans = []
peo = list(range(1, n + 1))

i = 0
while peo:
  i = (i + k - 1) % len(peo)
  ans.append(str(peo.pop(i)))

print(f"<{', '.join(ans)}>")