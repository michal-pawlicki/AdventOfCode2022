file = open("data", "r")
lines = file.readlines()
result = 0
for line in lines:
    arr = [i.split('-') for i in line.strip().split(",")]
    A = set(range(int(arr[0][0]), int(arr[0][1])+1))
    B = set(range(int(arr[1][0]), int(arr[1][1])+1))
    if A.intersection(B) or B.intersection(A):
        result += 1
print(result)
