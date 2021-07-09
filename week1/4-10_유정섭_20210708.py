save = {}
def fivo(n):
  try:
    return save[n]
  except KeyError:
    save[n] = fivo(n-1) + fivo(n-2) if n >= 3 else n
    return save[n]

answer = []
while True:
  a, b = [int(x) for x in input().split()]
  if a == b == 0:
    break
  n = 1
  cnt = 0
  while fivo(n) <= b: 
    if fivo(n) >= a: cnt+=1
    n+= 1
  answer.append(cnt)

for ans in answer:
  print(ans)