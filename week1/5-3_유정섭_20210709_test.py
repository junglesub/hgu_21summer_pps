s = set()
inp = "4177252841" # 1234567890
k = 9
result = 0

k_range = 1
for i in range(k):
  k_range *= (len(inp) - i)
print(k_range)

for i in range(k_range):
  idxes = []
  for j in range(k):
    idxes.append(i % (len(inp) - j))
  
  if len(set(idxes)) == k:
    s.add(tuple(sorted(tuple(idxes))))

for ids in s:
  print(ids)
  tst = inp
  for i in ids:
    tst = tst[:int(i)] + '_' + tst[int(i) + 1:]
  print(tst)
  tst = tst.replace("_", "")
  if int(tst) > result: result = int(tst)

print(result)
print(len(s))