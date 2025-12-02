import re

PUZZLE = open("input.txt").read().strip().split(",")
PART_1, PART_2 = 0, 0

def is_invalid(num, part_2=False):
    s = str(num)
    L = len(s)
    middle = L // 2
    if part_2:
        for i in range(1, middle + 1):
            chunks = re.findall(fr".{{1,{i}}}", num)
            if len(set(chunks)) == 1:
                return True

    if L & 1:
        return False
    left, right = num[:middle], num[middle:]
    if left == right:
        return True
    
    return False


for line in PUZZLE:
    start, end = (map(int,(line.split("-"))))
    for num in range(start, end + 1):
        if is_invalid(str(num)):
            PART_1 += num
        if is_invalid(str(num), True):
            PART_2 += num

print("PART 1:", PART_1)
print("PART 2:", PART_2)