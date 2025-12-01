
PUZZLE = [line.strip() for line in open("input.txt")]
DIAL = 50
LENGTH = 100
PART_1, PART_2 = 0, 0

def simulate(stepwise=False):
    dial = 50
    count = 0

    for instruction in PUZZLE:
        dir, move = instruction[0], int(instruction[1:])
        delta = -1 if dir == "L" else +1

        if stepwise:
            for _ in range(move):
                dial = (dial + delta) % LENGTH 
                if dial == 0:
                    count += 1
        else:
            dial = (dial + delta * move) % LENGTH
            if dial == 0:
                count += 1
    return count

print("PART_1:", simulate())
print("PART_2:", simulate(stepwise=True))