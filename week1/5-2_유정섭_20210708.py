tc = int(input())

answer = []
for _ in range(tc):
  eq = input().replace("@", "*3").replace("%", "+5").replace("#", "-7").split()
  ans = float(eq[0])
  for e in eq[1:]:
    ans = eval(str(ans) + e)
  answer.append(ans)

for ans in answer:
  print("%.2f" % ans)