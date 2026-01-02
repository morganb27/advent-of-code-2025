INTERVALS, INGREDIENTS = open("input.txt").read().strip().split("\n\n")

INTERVALS = [tuple(map(int, line.split("-"))) for line in INTERVALS.splitlines()]
INGREDIENTS = map(int, INGREDIENTS.splitlines())
PART_1 = 0

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x : x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(end, last_end))
        else:
            merged.append((start, end))

    return merged

MERGED_INTERVALS = merge_intervals(INTERVALS)

def is_fresh(x):
    for a, b in MERGED_INTERVALS:
        if a <= x <= b:
            return True
    return False


for ingredient in INGREDIENTS:
    if is_fresh(ingredient):
        PART_1 += 1

print("PART_1:", PART_1)
print("PART_2:", sum(b - a + 1 for a, b in MERGED_INTERVALS))