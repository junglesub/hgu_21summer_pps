data = [int(d) for d in input().split()]
sort_data = sorted(data)

if data == sort_data:
    print("ascending")
elif data == sort_data[::-1]:
    print("descending")
else:
    print("mixed")
