import os

datapath = os.path.join("data", "day2.txt")

def get_score_pick(your_pick):
    score = 0
    if your_pick == "X":
        score += 1
    elif your_pick == "Y":
        score += 2
    elif your_pick == "Z":
        score += 3
    return score

def get_score_match(opponent_pick, your_pick):
    # If equal
    if ord(opponent_pick) == ord(your_pick)-23:
        return 3
    if your_pick == "X":
        if opponent_pick == "B":
            return 0
        elif opponent_pick == "C":
            return 6
    if your_pick == "Y":
        if opponent_pick == "A":
            return 6
        elif opponent_pick == "C":
            return 0
    if your_pick == "Z":
        if opponent_pick == "A":
            return 0
        elif opponent_pick == "B":
            return 6

def decode_part2(opponent_pick, your_pick):

    if your_pick == "X":
        if opponent_pick == "A":
            return "Z"
        elif opponent_pick == "B":
            return "X"
        elif opponent_pick == "C":
            return "Y"
    if your_pick == "Y":
        if opponent_pick == "A":
            return "X"
        elif opponent_pick == "B":
            return "Y"
        elif opponent_pick == "C":
            return "Z"
    if your_pick == "Z":
        if opponent_pick == "A":
            return "Y"
        elif opponent_pick == "B":
            return "Z"
        elif opponent_pick == "C":
            return "X"

def get_score_part1(opponent_pick, your_pick):
    score = get_score_match(opponent_pick, your_pick) + get_score_pick(your_pick)
    return score

def get_score_part2(opponent_pick, your_pick):
    your_pick = decode_part2(opponent_pick, your_pick)
    score = get_score_match(opponent_pick, your_pick) + get_score_pick(your_pick)
    return score

## Part 1
with open(datapath) as f:
    lines = f.readlines()

lines = [(x.strip().split(" ")) for x in lines]
# total_score = 0
# for i,j in lines:
#     total_score += get_score_part1(i,j)
# print(total_score)

## Part 2
with open(datapath) as f:
    lines = f.readlines()

lines = [(x.strip().split(" ")) for x in lines]
total_score = 0
for i,j in lines:
    total_score += get_score_part2(i,j)
print(total_score)
