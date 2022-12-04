file = open("data", "r")
lines = file.readlines()
result = 0
list_of_threes = [lines[i:i+3] for i in range(0, len(lines), 3)]

for group in list_of_threes:
    for element in "".join(set(group[0].strip())):
        if element in group[1]:
            if element in group[2]:
                if element.isupper():
                    result += ord(element) - 38
                else:
                    result += ord(element) - 96
print(result)
