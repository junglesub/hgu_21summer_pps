cnt = {}
for c in input().upper():
  if c not in cnt.keys():
    cnt[c] = 0
  cnt[c] += 1
values = sorted(cnt.values(), reverse=True)
if len(values) != 1 and values[0] == values[1]:
  print("?")
else:
  print(next(k for k, v in cnt.items() if v is values[0]))
