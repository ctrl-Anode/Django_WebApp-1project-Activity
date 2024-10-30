numbers = (1, 3, 2, 4, 3, 1, 2, 5)
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1
for num, count in counts.items():
    if count > 1:
        print(num)