def solution(dirs):
  visited = set()
  last = [0, 0]

  for c in dirs:
    old_last = list(last) # deep copy
    if c == "U" and last[1] < 5: last[1] += 1
    elif c == "D" and last[1] > -5: last[1] -= 1
    elif c == "R" and last[0] < 5: last[0] += 1
    elif c == "L" and last[0] > -5: last[0] -= 1
    else: print(c, "Invalid")
    # 생각이 약간 꼬였는데, 움직였을 때만 이동한 내역에 추가.
    if old_last != last: visited.add(str(sorted([old_last, last])))
  print(visited)
  return len(visited)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LRLR"))