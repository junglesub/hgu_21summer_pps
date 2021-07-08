key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value = "DEFGHIJKLMNOPQRSTUVWXYZABC"
dic = dict(zip(value, key))
for c in input():
  print(dic[c], end="")