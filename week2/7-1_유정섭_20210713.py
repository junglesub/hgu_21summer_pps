n = int(input())
ageList = []
for _ in range(n):
  ageList.append(input().split())
print("\n".join(map(lambda x: ' '.join(x), sorted(ageList, key=lambda x: int(x[0])))))