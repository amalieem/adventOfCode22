with open("input.txt") as file:
    data = file.read().split("\n")

def setPathInFileHierarchy(path: list[str], filehierarchy: dict | int, size: int):
    tempDict = filehierarchy
    for dir in path[:-1]:
        if (dir not in tempDict):
            tempDict[dir] = {}
        tempDict = tempDict[dir]
    tempDict[path[-1]] = size

root = {}
path = [ "/" ]

for line in data:
    splitLine = line.split(" ")
    if line == "$ cd ..":
        path.pop()
    elif line == "$ cd /":
        pass
    elif line[0:4] == "$ cd":
        path.append(splitLine[-1])
    elif line == "$ ls":
        pass
    elif splitLine[0] == "dir":
        pass
    else:
    #   print(f"Using line '{line}' to set path {path} with file {splitLine[1]}")
      setPathInFileHierarchy(path + [splitLine[1]], root, int(splitLine[0]))
    #   print("new file hiearachy")
    #   print(root)

def sizeOf(value: dict | int) -> int:
    if isinstance(value, dict):
        return sum(sizeOf(subvalue) for subvalue in value.values())
    else:
        return value

def calculateDirSizes(value: dict) -> list[int]:
    sizes = []
    for maybeDir in value.values():
        if isinstance(maybeDir, dict):
            sizes.append(sizeOf(maybeDir))
            sizes += calculateDirSizes(maybeDir)
    return sizes

sizes = calculateDirSizes(root)

# Part 1
dirs = []
for dirSize in sizes:
    if dirSize < 100000:
        dirs.append(dirSize)
print(sum(dirs))

# Part 2
totalUsedSpace = sizes[0]
unusedSpace = 70000000 - totalUsedSpace
neededSpace = 30000000
mustBeDeleted = neededSpace - unusedSpace

possibleDirs = []
for dirSize in sizes:
    if dirSize > mustBeDeleted:
        possibleDirs.append(dirSize)

print(min(possibleDirs))
