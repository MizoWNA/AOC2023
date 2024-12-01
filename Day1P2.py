# Still doesnt work for some odd reason, even though it should


preraw = open("day1.txt", "r").read().splitlines()

raw = []

def preprocesser(item):
    replacements = {
        "one": "1", "two": "2", "three": "3", "four": "4", "zero":"0",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    for word, digit in replacements.items():
        item = item.replace(word, digit)
    return item



for i in preraw:
    raw.append(preprocesser(i))


processed = []

numbs = "1234567890"
curr = ''

for item in raw:
    curr = ''
    for letter in item:
        if letter in numbs:
            curr = curr + letter
    processed.append(curr)


secondround = []

for i in processed:
    secondround.append(i[0] + i[-1])

print(sum(list(map(int, secondround))))

