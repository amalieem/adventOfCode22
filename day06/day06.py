with open("input.txt") as file:
    data = file.read()

def uniqeChars(n):
    marker = 0
    for i in range(n, len(data)+1):
        chars = data[i-n:i]
        if (len(set(chars))) == n:
            marker = i
            break
    return marker

answer1 = uniqeChars(4)
answer2 = uniqeChars(14)

print(answer1, answer2)