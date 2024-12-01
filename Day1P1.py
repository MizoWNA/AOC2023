raw = open("day1.txt", "r").read().splitlines()

processed = []

numbs = "1234567890"

curr = ''

for item in raw:
    for letter in item:
        if letter in numbs:
            curr = curr + letter
    processed.append(curr)
    curr = ''

processed2 = []

for i in processed:
    processed2.append(i[0] + i[-1])

final = list(map(int, processed2))

print(sum(final))