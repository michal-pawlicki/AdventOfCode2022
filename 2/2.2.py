file = open("data", "r")
lines = file.readlines()

score = 0
M = [["Z", "X", "Y"],
     ["X", "Y", "Z"],
     ["Y", "Z", "X"]]

for line in lines:
    temp = line.split()
    score += (0 if temp[1] == "X" else 3 if temp[1] == "Y" else 6)
    you = M[(0 if temp[1] == "X" else 1 if temp[1] == "Y" else 2)][(0 if temp[0] == "A" else 1 if temp[0] == "B" else 2)]
    score += (1 if you == "X" else 2 if you == "Y" else 3)

print(score)
