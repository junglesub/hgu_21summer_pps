# 많이 마음에 안든다..
# 공식 이나 그런것을 활용해서 한번에 할 수 있을거 같다.

n = int(input())
first = int(input())
trip = []
last = first
failed = False

for i in range(2, n + 1):
  # 2의 배수 문은 항상 첫번째 문과 반대이다.
  if i % 2 == 0 and last != first:
    failed = True
    break
  # 3의 배수 문은 항성 첫번째 문과 같다.
  if i % 3 == 0 and last == first:
    failed = True
    break
  last = (last + 1) % 2
  trip.append(str(last))

if failed:
  print("Love is open door")
else:
  print("\n".join(trip))
  