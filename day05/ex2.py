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

def moveMultipleCarts(times, fromS, toS):
    temp = []
    for i in range(times):
        cart = stacks[fromS].pop()
        temp.append(cart) 
        
    stacks[toS] += (temp[::-1])

for line in moves:
    words = line.split()
    moveMultipleCarts(int(words[1]), int(words[3])-1, int(words[5])-1)

res = ""
for line in stacks:
    res += line[-1]

print(res)