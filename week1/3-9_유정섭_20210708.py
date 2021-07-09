sentence = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()

nth = int(input()) - 1
word = sentence[nth % len(sentence)]

if word in ["tururu", "turu"]:
  word += ("ru" * int(nth / len(sentence)))
  cnt = word.count("ru")
  if cnt >= 5: word = f"tu+ru*{cnt}"

print(word)