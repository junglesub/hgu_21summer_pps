input()
num = set(map(int, input().split()))
input()
for x in input().split(): print("1" if int(x) in num else "0")
