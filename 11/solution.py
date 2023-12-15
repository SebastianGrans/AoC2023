#%%
#%%
from copy import deepcopy


raw_data = list(map(str.rstrip, open("example_input").readlines()))

#%%
rows = 0
cols = len(raw_data[0])
empty_row_idxs = []

exansion_factor = 1

galaxies = []
row_expansion = 0
for ridx, line in enumerate(raw_data):
    rows = ridx
    added_galaxies = 0
    for cidx, char in enumerate(line):
        if char == "#":
            galaxies.append([ridx + (row_expansion*exansion_factor), cidx])
            added_galaxies += 1
        
    if added_galaxies == 0:
        empty_row_idxs.append(ridx)
        row_expansion += 1


#%%
# Find emtpy cols
all_cols = set(range(cols))
all_galaxy_cols = set([galaxy[1] for galaxy in galaxies])
empty_col_idxs = list(all_cols - all_galaxy_cols)
empty_col_idxs.sort()
# %%
# update galaxy col coordinates
#galaxies.sort(key=lambda x: x[1])
col_expansion = []
last_col = 0
expansion = 0
for empty_col in empty_col_idxs:
    col_expansion += [expansion]*(empty_col - last_col)*exansion_factor
    last_col = empty_col
    expansion += 1

col_expansion += [expansion]*(cols - last_col)*exansion_factor
# %%
for galaxy in galaxies:
    galaxy[1] = galaxy[1]+col_expansion[galaxy[1]] 

# %%

def manhattan_dist(start, end) -> int:
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

#%%


#%%
galaxiess = deepcopy(galaxies)

dists = []
while len(galaxiess) > 1:
    galaxy1 = galaxiess.pop()

    for galaxy2 in galaxiess:
        dists.append(manhattan_dist(galaxy1, galaxy2))
    

print(f"sum dist {sum(dists)}")
# %%


