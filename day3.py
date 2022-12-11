import os

datapath = os.path.join("data", "day3.txt")
with open(datapath) as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]


def find_duplicate_item(rucksack):
    comp_1, comp_2 = rucksack
    for i in comp_1:
        if i in comp_2:
            return i

def find_batch_item(rucksack_1, rucksack_2, rucksack_3):
    for i in rucksack_1:
        if (i in rucksack_2) and (i in rucksack_3):
            return i

def get_value(item):
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96


## Part 1
# total = 0
# lines = [(x[:int(len(x)/2)], x[int(len(x)/2):len(x)]) for x in lines]
# for line in lines:
#     item = find_duplicate_item(line)
#     total += get_value(item)
# print(total)

## Part 2
batch = []
total = 0
for i,line in enumerate(lines):
    batch.append(line)
    if i%3 == 2:
        item = find_batch_item(*batch)
        batch = []
        total += get_value(item)

print(total)
