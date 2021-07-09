from subprocess import Popen, PIPE, STDOUT, run
import random

tested = set()

i = 0
alreadyTested = 0

while alreadyTested < 10:
  tc = a, b, c = [random.randint(0, 15) for _ in range(3)]
  test = ('a' * a) + ('b' * b) + ('c' * c)

  if tuple(tc) in tested:
    alreadyTested+=1
    continue

  alreadyTested = 0
  tested.add(tuple(tc))
  
  pmy = run(['./5-10_유정섭_20210709.my.o'], stdout=PIPE,
        input=f'2\n{test}\n{test}\n', encoding='ascii')
  my = pmy.stdout.strip()
  pans = run(['./5-10_유정섭_20210709.ans.o'], stdout=PIPE,
        input=f'2\n{test}\n{test}\n', encoding='ascii')
  ans = pans.stdout.strip()

  print(f"TC #{i} : a={a} b={b} c={c} :: {test}")
  print("MY:", my, "ANS:", ans)
  print("Match:", my == ans)
  print()
  # break
  if my != ans: break