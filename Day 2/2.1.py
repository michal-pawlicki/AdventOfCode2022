file = open("data", "r")
lines = file.readlines()

score = 0
M = [[3, 6, 0],
     [0, 3, 6],
     [6, 0, 3]]

for line in lines:
    temp = line.split()
    score += (1 if temp[1] == "X" else 2 if temp[1] == "Y" else 3)
    score += M[(0 if temp[0] == "A" else 1 if temp[0] == "B" else 2)][(0 if temp[1] == "X" else 1 if temp[1] == "Y" else 2)]

print(score)
