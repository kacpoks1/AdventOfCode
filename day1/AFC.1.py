file = open("/home/kacper/Dokumenty/AdventOfCode/day1/AFC.1.txt",'r')

data = file.read()

data = data.strip().split("\n")

first = []
second = []

for line in data:
    line = line.strip().split(" ")
    first.append(line[0])
    second.append(line[-1])


score = 0

for num in first:
    score += int(num) * second.count(num)


print(score)