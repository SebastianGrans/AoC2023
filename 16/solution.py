
#%%

from copy import deepcopy
from enum import Enum
import re

#%%

# raw_data = open("example_input").readlines()
raw_data = []
raw_data_rows = 0
raw_data_cols = 0
with open("example_input") as file:
    ridx = 0
    line = file.readline()
    raw_data_cols = len(line) - 1 # because newline
    while line:
        line = line.rstrip()
        # print(line)
        new_line = line.replace("\\", "L")
        raw_data.append(new_line)
        # print(f"{new_line} {len(new_line)}")
        # print("")
        ridx += 1
        line = file.readline()

    raw_data_rows = ridx

## Naive solution instead.Stepping

def pm(mapp, visited_map):
    cols = "".join(str(x) for x in range(len(mapp[0])))
    print(f" {cols} {cols}")
    for ridx, (mline, vline) in enumerate(zip(mapp, visited_map)):
        print(f"{ridx}{mline} {vline}")


def step(beam):
    beam[0][0] += beam[1][0]
    beam[0][1] += beam[1][1]

class Dir(list, Enum):
    UP = [-1, 0]
    RIGHT = [0, 1]
    DOWN = [1, 0]
    LEFT = [0, -1]
#%%

pattern = r"(\||-|L|\/){1}"

mirrors = {}
for ridx, line in enumerate(raw_data):
    matches = re.finditer(pattern, line)
    for m in matches:
        if m.group(1) in "|-":
            mirrors[(ridx, m.start())] = False
        if m.group(1) in "L/":
            mirrors[(ridx, m.start())] = [False]*4



beams = [[[0, -1], Dir.RIGHT]]
mapp = deepcopy(raw_data)
while beams:
    #pm(raw_data, mapp)
    beam = beams.pop()
    
    row, col = beam[0]
    dirr = beam[1]
    #print(f"Current beam: ({row}, {col}) {dirr}")
    step(beam)
    row, col = loc = deepcopy(beam[0])
    dirr = beam[1]
    #print(f"After step: ({row}, {col})")
    if not (0 <= row < raw_data_rows) or not (0 <= col < raw_data_cols):
        #print(f"Beam outside of field ({row}, {col}) {dirr}")
        # outside the board
        continue
    #print(len(beams))
    # if mapp[row][col] in "#":
    #     mapp[row] = mapp[row][:col] + "+" + mapp[row][col+1:]
    # elif mapp[row][col] in "+.":
    char = "#" #if mapp[row][col] != "#" else "+"
    mapp[row] = mapp[row][:col] + char + mapp[row][col+1:]
    
    match raw_data[row][col]:
        case "-" if dirr == Dir.UP or dirr == Dir.DOWN:
            if mirrors[tuple(loc)]:
                continue
            beams.extend([[deepcopy(loc), Dir.LEFT], [loc, Dir.RIGHT]])
            mirrors[tuple(loc)] = True
        case "|" if dirr == Dir.LEFT or dirr == Dir.RIGHT:
            if mirrors[tuple(loc)]:
                continue
            beams.extend([[deepcopy(loc), Dir.UP], [loc, Dir.DOWN]])
            mirrors[tuple(loc)] = True
        case "/":
            match dirr:
                case Dir.UP:
                    if not mirrors[tuple(loc)][0]:
                        beams.append([loc, Dir.RIGHT])
                        mirrors[tuple(loc)][0] = True
                case Dir.RIGHT:
                    if not mirrors[tuple(loc)][1]:
                        beams.append([loc, Dir.UP])
                        mirrors[tuple(loc)][1] = True
                case Dir.DOWN:
                    if not mirrors[tuple(loc)][2]:
                        beams.append([loc, Dir.LEFT])
                        mirrors[tuple(loc)][2] = True
                case Dir.LEFT:
                    if not mirrors[tuple(loc)][3]:
                        beams.append([loc, Dir.DOWN])
                        mirrors[tuple(loc)][3] = True
        case "L":
            match dirr:
                case Dir.UP:
                    if not mirrors[tuple(loc)][0]:
                        beams.append([loc, Dir.LEFT])
                        mirrors[tuple(loc)][0] = True
                case Dir.RIGHT:
                    if not mirrors[tuple(loc)][1]:
                        beams.append([loc, Dir.DOWN])
                        mirrors[tuple(loc)][1] = True
                case Dir.DOWN:
                    if not mirrors[tuple(loc)][2]:
                        beams.append([loc, Dir.RIGHT])
                        mirrors[tuple(loc)][2] = True
                case Dir.LEFT:
                    if not mirrors[tuple(loc)][3]:
                        beams.append([loc, Dir.UP])
                        mirrors[tuple(loc)][3] = True
        case _:
            beams.append(beam)

    #print("hodl")

# %%
            
from collections import Counter
print(f"Solution task 1: {Counter("".join(mapp))["#"]}")

# %%

#%% 

# task 2

def ray(raw_data, beams) -> int:
    pattern = r"(\||-|L|\/){1}"

    mirrors = {}
    for ridx, line in enumerate(raw_data):
        matches = re.finditer(pattern, line)
        for m in matches:
            if m.group(1) in "|-":
                mirrors[(ridx, m.start())] = False
            if m.group(1) in "L/":
                mirrors[(ridx, m.start())] = [False]*4


    mapp = deepcopy(raw_data)
    while beams:
        #pm(raw_data, mapp)
        beam = beams.pop()
        
        row, col = beam[0]
        dirr = beam[1]
        #print(f"Current beam: ({row}, {col}) {dirr}")
        step(beam)
        row, col = loc = deepcopy(beam[0])
        dirr = beam[1]
        #print(f"After step: ({row}, {col})")
        if not (0 <= row < raw_data_rows) or not (0 <= col < raw_data_cols):
            #print(f"Beam outside of field ({row}, {col}) {dirr}")
            # outside the board
            continue
        #print(len(beams))
        # if mapp[row][col] in "#":
        #     mapp[row] = mapp[row][:col] + "+" + mapp[row][col+1:]
        # elif mapp[row][col] in "+.":
        char = "#" #if mapp[row][col] != "#" else "+"
        mapp[row] = mapp[row][:col] + char + mapp[row][col+1:]
        
        match raw_data[row][col]:
            case "-" if dirr == Dir.UP or dirr == Dir.DOWN:
                if mirrors[tuple(loc)]:
                    continue
                beams.extend([[deepcopy(loc), Dir.LEFT], [loc, Dir.RIGHT]])
                mirrors[tuple(loc)] = True
            case "|" if dirr == Dir.LEFT or dirr == Dir.RIGHT:
                if mirrors[tuple(loc)]:
                    continue
                beams.extend([[deepcopy(loc), Dir.UP], [loc, Dir.DOWN]])
                mirrors[tuple(loc)] = True
            case "/":
                match dirr:
                    case Dir.UP:
                        if not mirrors[tuple(loc)][0]:
                            beams.append([loc, Dir.RIGHT])
                            mirrors[tuple(loc)][0] = True
                    case Dir.RIGHT:
                        if not mirrors[tuple(loc)][1]:
                            beams.append([loc, Dir.UP])
                            mirrors[tuple(loc)][1] = True
                    case Dir.DOWN:
                        if not mirrors[tuple(loc)][2]:
                            beams.append([loc, Dir.LEFT])
                            mirrors[tuple(loc)][2] = True
                    case Dir.LEFT:
                        if not mirrors[tuple(loc)][3]:
                            beams.append([loc, Dir.DOWN])
                            mirrors[tuple(loc)][3] = True
            case "L":
                match dirr:
                    case Dir.UP:
                        if not mirrors[tuple(loc)][0]:
                            beams.append([loc, Dir.LEFT])
                            mirrors[tuple(loc)][0] = True
                    case Dir.RIGHT:
                        if not mirrors[tuple(loc)][1]:
                            beams.append([loc, Dir.DOWN])
                            mirrors[tuple(loc)][1] = True
                    case Dir.DOWN:
                        if not mirrors[tuple(loc)][2]:
                            beams.append([loc, Dir.RIGHT])
                            mirrors[tuple(loc)][2] = True
                    case Dir.LEFT:
                        if not mirrors[tuple(loc)][3]:
                            beams.append([loc, Dir.UP])
                            mirrors[tuple(loc)][3] = True
            case _:
                beams.append(beam)

    return Counter("".join(mapp))["#"]


#%%
    
fromtop = [[[-1, x], [1, 0]] for x in range(raw_data_cols)]
fromright = [[[x, raw_data_cols], [0, -1]] for x in range(raw_data_rows)]
frombottom = [[[raw_data_rows, x], [-1, 0]] for x in range(raw_data_cols)]
fromleft = [[[x, -1], [0, 1]] for x in range(raw_data_rows)]

starting_pos = fromtop + fromright + frombottom + fromleft

#%%

max_lava = 0
for start in starting_pos:
    max_lava = max(max_lava, ray(raw_data, [deepcopy(start)]))
# %%
print(f"Solution task 2: {max_lava}")
# %%
