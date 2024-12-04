with open("/home/kacper/Dokumenty/AdventOfCode/day1/AFC.1.txt", 'r') as file:
    data = file.read().strip().split("\n")

left = []
right = []

for line in data:
    numbers = line.strip().split()  # Rozdziel linie według białych znaków
    left.append(int(numbers[0]))  # Pierwsza liczba
    right.append(int(numbers[1]))  # Druga liczba

# Sortowanie obu list
left.sort()
right.sort()

# Obliczanie całkowitej odległości
score = sum(abs(left - right) for left, right in zip(left, right))

print(score)
