scores = {"X":1, "Y":2, "Z":3} #Rock, Paper, Scissors
wins = ["C X", "B Z", "A Y"]
draws = ["A X", "B Y", "C Z"]
totalScore = 0

with open("input.txt") as file:
    data = file.read().split("\n")

for i in data:
    if i in wins:
        totalScore += 6
    elif i in draws:
        totalScore += 3
    scoresKey = i[2]
    totalScore += scores[scoresKey]

print("Total score according to strategy guide: " + str(totalScore))