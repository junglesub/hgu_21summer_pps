result = []
for i in range(int(input())):
  result.append([ord(c) + 1 for c in input()])
for i, r in enumerate(result):
  print(f"String #{i + 1}")
  print("".join([chr((a - 65) % 26 + 65) for a in r]))
  if i + 1 != len(result):
    print()