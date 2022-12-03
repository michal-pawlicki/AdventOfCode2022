file = open("data", "r")
lines = file.readlines()
result = 0
for line in lines:
    for element in "".join(set([*line[len([*line])//2:]])):
        if element in line[0:len([*line])//2]:
            if element.isupper():
                result += ord(element) - 38
            else:
                result += ord(element) - 96
print(result)
