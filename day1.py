import os

datapath = os.path.join("data", "day1.txt")

## Part 1
with open(datapath) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
max_val = 0
val = 0
for line in lines:
    if not line:
        val = 0
    else:
        val += int(line)
    max_val = max(max_val, val)
print("Part 1" ,max_val)

## Part 2
with open(datapath) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
values = []
val = 0
for line in lines:
    if not line:
        values.append(val)
        val = 0
    else:
        val += int(line)
values.sort(reverse=True)
print(sum(values[0:3]))
