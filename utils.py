import re
from dataclasses import dataclass
from functools import reduce
import operator
from itertools import groupby


#re.findall(r"(\d+) (\w+) (\w+)"

#[b - a for a, b in zip(p, p[1:])]

#hash = hashlib.md5(s.encode("utf-8")).hexdigest()
#print(hash)  Output: 5d41402abc4b2a76b9719d911017c592
#parsed = ast.literal_eval(line)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __add__(self, right_side: 'Point') -> 'Point':
        return Point(self.x + right_side.x, self.y + right_side.y)
    
    def __sub__(self, right_side: 'Point') -> 'Point':
        return Point(self.x - right_side.x, self.y - right_side.y)
    
    def __mul__(self, factor: 'int') -> 'Point':
        return Point(self.x * factor, self.y * factor)
    
    def neighbours_4(self) -> list['Point']:
        return [self + d for d in DIRS_4]
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    

DIRS_8 = [
    Point(0, 1),   #N
    Point(1, 1),   #NE
    Point(1, 0),   #E
    Point(-1, 1),  #SE
    Point(0, -1),  #S
    Point(-1, -1), #SW
    Point(-1, 0),  #W
    Point(1, -1)   #NW
]

DIRS_4 = [
    Point(0, -1),  # N 
    Point(1, 0),   # E 
    Point(0, 1),   # S 
    Point(-1, 0),  # W 
]

def rotate_right(x, y, times):
    for _ in range(times):
        x, y = y, -x
    return x, y


DIRECTION = {
    "N": lambda x, y, steps: Point(x, y + steps),
    "S": lambda x, y, steps: Point(x, y - steps),
    "E": lambda x, y, steps: Point(x + steps, y),
    "W": lambda x, y, steps: Point(x - steps, y)
}

def mul(list):
    return reduce(operator.mul, list, 1)


def union_group(group): 
    return set.union(*map(set, group.split("\n")))

def intersection_group(group): 
    return set.intersection(*map(set, group.split("\n")))

def extract_words(s, words):
    pattern = r"\b(" + "|".join(re.escape(w) for w in words) + r")\b"
    return re.findall(pattern, s)

def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", s)))

def ints_positives(s: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))

def two_sum(nums, target):
    cache = set()
    
    for num in nums:
        delta = target - num
        if delta in cache:
            return num, delta
        cache.add(num)
    return None

def process(s):
    sequence = ""
    for key, group in groupby(s):
        sequence += str(len(list(group))) + key
    return sequence

def three_sum(nums, target):
    nums.sort()

    for i, num in enumerate(nums):
        subarray = nums[i+1:]
        left, right = 0, len(subarray) - 1
        delta = target - num

        while left < right:
            sum = subarray[left] + subarray[right]
            if sum == delta:
                return num, subarray[left], subarray[right]
            if sum > delta:
                right -= 1
            else:
                left += 1
    return None

