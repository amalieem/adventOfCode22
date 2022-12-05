with open("input.txt") as file:
    [init, moves] = file.read().split("\n\n")

init = init.split("\n")
moves = moves.split("\n")

stacks = []
stackCount = int(init[-1].strip().split(" ")[-1])
for i in range(stackCount):
    stacks.append([])

init = init[:-1]
for line in init[::-1]:
    for x in range(1, len(line), 4):
        if line[x] != " ":
            stackIndex = (x-1)//4
            stacks[stackIndex].append(line[x])

def moveOneCart(fromS, toS):
    cart = stacks[fromS].pop()
    stacks[toS].append(cart)

for line in moves:
    words = line.split()
    for i in range(int(words[1])):
        moveOneCart(int(words[3])-1, int(words[5])-1)

res = ""
for line in stacks:
    res += line[-1]

print(res)