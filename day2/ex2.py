scores = {"A": 1, "B":2, "C":3} #Rock, Paper, Scissors
wins = ["C A", "B C", "A B"]
loss = ["A C", "C B", "B A"]
totalScore = 0

with open("input.txt") as file:
    data = file.read().split("\n")

for i in data:
    opponent = i[0]
    myMove = 0
    if i[2] == "X": # Loss
        for j in loss:
            if j[0] == opponent:
                myMove = j[2]
    elif i[2] == "Y": # Draw
        totalScore += 3
        myMove = opponent
    else: # Win
        totalScore += 6
        for j in wins:
            if j[0] == opponent:
                myMove = j[2]
    totalScore += scores[myMove]

print("Total score according to strategy guide: " + str(totalScore))