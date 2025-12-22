from utils import Point, DIRS_8

PUZZLE = [line.strip() for line in open("input.txt")]
POS = set()
PART_1 = 0
TOTAL = 0

for row in range(len(PUZZLE)):
    for col in range(len(PUZZLE[row])):
        if PUZZLE[row][col] == "@":
            POS.add(Point(col, -row))


def remove(pos):
    res = 0
    new_pos = set()
    for roll in pos:
        count = 0
        for dir in DIRS_8:
            if roll + dir in pos:
                count += 1
        if count < 4:
            res += 1
        else:
            new_pos.add(roll)
    return res, new_pos


while True:
    current, POS = remove(POS)
    if TOTAL == 0:
        print("PART_1:", current)
    TOTAL += current
    if current == 0:
        print("PART_2:", TOTAL)
        break


