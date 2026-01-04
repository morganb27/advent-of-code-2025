PUZZLE = [line.strip() for line in open("input.txt")]

MATRIX = [list(map(int, row.split())) for row in PUZZLE[:-1]]
OPERATORS = PUZZLE[-1].split()
PART_1 = 0

for col in range(len(MATRIX[0])):
    operator = OPERATORS[col]
    total = 0 if operator == "+" else 1
    for row in range(len(MATRIX)):
        if operator == "+":
            total += MATRIX[row][col]
        else:
            total *= MATRIX[row][col]
    PART_1 += total

print("PART_1:", PART_1)


