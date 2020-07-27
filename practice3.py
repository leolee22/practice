a = []
with open("fruit.txt", "r") as f:
    for line in f:
        a.append(line.strip())
print(a)
