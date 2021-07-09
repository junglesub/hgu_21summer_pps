def solution(number, k):
    s = set()
    result = 0

    k_range = 1
    for i in range(k):
      k_range *= (len(number) - i)

    for i in range(k_range):
      idxes = []
      for j in range(k):
        idxes.append(i % (len(number) - j))
      
      if len(set(idxes)) == k:
        s.add(tuple(sorted(tuple(idxes))))

    for ids in s:
      tst = number
      for i in ids:
        tst = tst[:int(i)] + '_' + tst[int(i) + 1:]
      tst = tst.replace("_", "")
      if int(tst) > result: result = int(tst)
    return str(result)

# TC
t1 = solution("4177252841", 4)
print(t1)

t1 = solution("1231234", 3)
print(t1)

'''
s = set()
number = "4177252841"
k = 4
result = 0

k_range = 1
for i in range(k):
  k_range *= (len(number) - i)
print(k_range)

for i in range(k_range):
  idxes = []
  for j in range(k):
    idxes.append(i % (len(number) - j))
  
  if len(set(idxes)) == k:
    s.add(tuple(sorted(tuple(idxes))))

for ids in s:
  print(ids)
  tst = number
  for i in ids:
    tst = tst[:int(i)] + '_' + tst[int(i) + 1:]
  print(tst)
  tst = tst.replace("_", "")
  if int(tst) > result: result = int(tst)

print(result)
print(len(s))
'''