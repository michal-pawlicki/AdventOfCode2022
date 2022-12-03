file = open("data", "r")
lines = file.readlines()
result = 0
for line in lines:
    arr1 = line[0:len([*line])//2]
    arr2 = [*line[len([*line])//2:]]
    for element in "".join(set(arr2)):
        if element in arr1:
            if element.isupper():
                result += ord(element) - 38
            else:
                result += ord(element) - 96
print(result)
