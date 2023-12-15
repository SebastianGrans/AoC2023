#%%

# raw_data = open("example_input").readlines()
raw_data = open("input").readlines()


#%%

maps = []
mapp = []
for line in raw_data:
    if line == "\n":
        maps.append(mapp)
        mapp = []
        continue
    mapp.append(line.rstrip())

maps.append(mapp)

#%%


def evaluate_candidate(mapp: list[list[int]], idx: int) -> bool:
    upper = mapp[idx::-1]
    lower = mapp[idx + 1:]
    #print_horiz(mapp, idx, ansi="\033[41m", ansi_reset="\033[0m")

    if all(map(lambda x: x[0] == x[1], zip(upper, lower))):

        return True

    return False


def find_vert_mirror(mapp: list[list[int]]) -> int:
    for ridx, (line1, line2) in enumerate(zip(mapp[:-1], mapp[1:])):
        if line1 == line2:
            if evaluate_candidate(mapp, ridx):
                return ridx

    return -1

def find_horiz_mirror(mapp: list[list[int]]) -> int:
    # hacky transponse
    return find_vert_mirror(list(zip(*mapp)))

#%%

#find_vert_mirror(maps[0])
# %%
#find_horiz_mirror(maps[0])
#%%

def print_join(mapp):
    for line in mapp:
        print("".join(line))


def print_horiz(mapp, idx, ansi="\033[7m", ansi_reset="\033[27m"):
    for ridx, line in enumerate(mapp):
        if ridx > idx:
            print("".join(line))
            continue
        print(ansi + "".join(line) + ansi_reset)

def print_vert(mapp, idx, ansi="\033[7m", ansi_reset="\033[27m"):
    for line in mapp:
        print(ansi + line[:idx+1] + ansi_reset + line[idx+1:])

# %%

cols_rows_sum = 0
for midx, mapp in enumerate(maps):
#for midx in [89, 90]:
    mapp = maps[midx]
    print(midx)
    col = find_horiz_mirror(mapp)
    row = find_vert_mirror(mapp)

    if col < 0 and row < 0:
        raise RuntimeError
    if col > 0 and row > 0:
        raise RuntimeError

    if col >= 0:
        cols_rows_sum += col+1
        print_vert(mapp, col)
    elif row >= 0:
        cols_rows_sum += (row+1)*100
        print_horiz(mapp, row)

    #input(">")
print(f"Sum: {cols_rows_sum}")



