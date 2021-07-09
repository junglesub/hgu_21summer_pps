winner = (0, 0)
for i in range(5):
  pt = sum([int(x) for x in input().split()])
  if winner[1] < pt: winner = (i + 1, pt)
print(winner[0], winner[1])

# sum_sc = []
# for i in range(5):
#   sum_sc.append(sum([int(x) for x in input().split()]))
# winner_score = max(sum_sc)
# print(sum_sc.index(winner_score) + 1, winner_score)
# 잠시만.. 굳이?