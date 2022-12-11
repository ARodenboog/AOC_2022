import os

def range_to_ints(range):
    start, end = range.split("-")
    start, end = int(start), int(end)
    return start, end

def fully_contains(range_1, range_2):
    start_1, end_1 = range_to_ints(range_1)
    start_2, end_2 = range_to_ints(range_2)

    min_start = min(start_2, start_1)
    max_end = max(end_1, end_2)
    if (min_start == start_2) and (max_end == end_2):
        return True
    elif (min_start == start_1) and (max_end == end_1):
        return True
    else:
        return False

def partly_contains(range_1, range_2):
    start_1, end_1 = range_to_ints(range_1)
    start_2, end_2 = range_to_ints(range_2)

    min_start = min(start_2, start_1)
    max_end = max(end_1, end_2)
    if (min_start == start_2):
        if start_1<= end_2:
            return True

    elif (min_start == start_1):
        if start_2 <= end_1:
            return True
    return False


datapath = os.path.join("data", "day4.txt")
with open(datapath) as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
lines = [(x.split(",")) for x in lines]
total = 0

## Part 1
for line in lines:
    total += fully_contains(line[0], line[1])
print(total)

## Part 2
total = 0
for line in lines:
    total += partly_contains(line[0], line[1])
print(total)
