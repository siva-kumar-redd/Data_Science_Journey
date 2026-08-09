ratings = [4, 5, 4, 3, 5, 4, 2]

frequency = {}

for rating in ratings:
    frequency[rating] = frequency.get(rating, 0) + 1

mode = max(frequency, key=frequency.get)

print(mode)



