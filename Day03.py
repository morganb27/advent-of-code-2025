from itertools import combinations

PUZZLE = [line.strip() for line in open("input.txt")]

PART_1, PART_2 = 0, 0



for line in PUZZLE:
    highest = 0
    for i in range(len(line) - 1):
        current = line[i] + max(line[i+1:])
        highest = max(int(current), highest)
    PART_1 += highest 

for line in PUZZLE:
    highest = 0
    print(line)
    for i in range(len(line) - 12):
        current, rest = line[i], line[i+1:]
        for comb in combinations(rest, 11):
            temp = current + "".join((str(num)) for num in comb)
            highest = max(int(temp), highest)
    PART_2 += highest 

print("PART_1:", PART_1)
print("PART_2:", PART_2)


