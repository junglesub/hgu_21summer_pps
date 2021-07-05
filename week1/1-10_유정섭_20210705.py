n = int(input())

cnt = {}

for i in range(n):
  let = input()[0]
  if let not in cnt.keys():
    cnt[let] = 0
  cnt[let] += 1

# 출력
res = []
for alpha, count in cnt.items():
  if count >= 5:
    res.append(alpha)
if(len(res) > 0):
  print("".join(sorted(res)))
else:
  print("PREDAJA")