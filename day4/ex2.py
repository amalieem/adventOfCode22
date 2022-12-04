with open("input.txt") as file:
    data = file.read().split("\n")

sum = 0
for i in range(len(data)):
    data[i] = data[i].split(",")
    for j in range(2):
        pair = data[i][j]
        indexdiv = pair.index("-")
        start = int(pair[:indexdiv])
        stop = int(pair[indexdiv + 1:])
        data[i][j] = list(range(start, stop + 1))

    check1 = any( item in data[i][0] for item in data[i][1])
    check2 = any( item in data[i][1] for item in data[i][0])
    if check1 or check2:
        sum += 1
    
print(sum)