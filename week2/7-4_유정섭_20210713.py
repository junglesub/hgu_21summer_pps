word = input()
suffix = [word[i:] for i in range(len(word))]
print("\n".join(sorted(suffix)))