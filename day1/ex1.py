with open("input.txt") as file:
    data = file.read().split("\n\n")

for i in range(len(data)):
    data[i] = data[i].split()
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

summedCalories = []
for i in data:
    summedCalories.append(sum(i))


print(max(summedCalories))

summedCalories.sort(reverse=True)
print(sum(summedCalories[:3]))
