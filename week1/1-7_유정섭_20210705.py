n, m = [int(s) for s in input().split()]

count = [0, 0, 0, 0, 0]
line_count = {}

for i in range(1 + n * 5):
  line = input()
  if "#####" in line:
    # count = [0, 0, 0, 0, 0] # Reset
    for w in line_count.values():
      count[w] += 1
    line_count = {}
    continue
  l_s = line.split("#")[1:-1]
  for i in range(m):
    s = l_s[i]
    if i not in line_count.keys():
        line_count[i] = 0
    if s == "****":
      line_count[i] += 1
  
print(" ".join([str(i) for i in count]))