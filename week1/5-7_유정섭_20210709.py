word = input()
count = 0

count += word.count("dz=")
word = word.replace("dz=", "_")

count += word.count("c=")
word = word.replace("c=", "_")

count += word.count("c-")
word = word.replace("c-", "_")

count += word.count("d-")
word = word.replace("d-", "_")

count += word.count("lj")
word = word.replace("lj", "_")

count += word.count("nj")
word = word.replace("nj", "_")

count += word.count("s=")
word = word.replace("s=", "_")

count += word.count("z=")
word = word.replace("z=", "_")

word = word.replace("_", "")
count += len(word)

print(count)