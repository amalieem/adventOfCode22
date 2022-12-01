with open("input.txt") as file:
    data = file.read().splitlines()
    caloriesPerElf = []
    elf = []
    for i in range(len(data)):
        if data[i] != "":
            elf.append((int(data[i])))
        else:
            caloriesPerElf.append(elf)
            elf = []
    caloriesPerElf.append(elf)

summedCalories = []
for i in caloriesPerElf:
    summedCalories.append(sum(i))


print(max(summedCalories))

summedCalories.sort(reverse=True)
print(sum(summedCalories[:3]))
