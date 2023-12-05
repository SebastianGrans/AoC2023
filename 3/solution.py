# %%
import re
from math import prod


#%%
raw_data = []
with open("input", "r") as f:
    for line in f:
        raw_data.append(line)

#%%
def number_in_neighborhood(part_location: tuple[int, int], numbers) -> list[int]:
    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = set()
    for offset in neighbor_offsets:
        coordinate = (part_location[0] + offset[0], part_location[1] + offset[1])
        try:
            neighbors.add(numbers[coordinate])
        except:
            continue

    return neighbors


#%%
def structure_data(raw_data) -> tuple[dict, dict]:
    numbers_pattern = r"(\d+)"
    parts_pattern = r"([^\.\d])"

    parts: dict[tuple[int, int], str] = {}
    numbers: dict[tuple[int, int], int] = {}
    for row_idx, line in enumerate(raw_data):
        row = line.rstrip()
        for match in re.finditer(parts_pattern, row):
            parts[(row_idx, match.start())] = match.group(1)
        
        for match in re.finditer(numbers_pattern, row):
            for col in range(match.span()[0], match.span()[1]):
                numbers[(row_idx, col)] = int(match.group(1))
    
    return parts, numbers

#%%
def solve1(raw_data) -> int:
    parts, numbers = structure_data(raw_data)
    all_numbers = []
    for part_location, part in parts.items():
        all_numbers += list(number_in_neighborhood(part_location, numbers))
    
    return sum(all_numbers)


#%% 
print(f"Solution task 1: {solve1(raw_data)}")
assert solve1(raw_data) == 539637

# %%
from timeit import timeit
n = 10000
results = timeit("solve1(raw_data)", number=n, setup="from __main__ import solve1", globals=globals())
print(f"Average time task 1: {(results/n) * 10**3} ms")
# Average time task 1: 2.5985688800006757 ms

#%%

def solve2(raw_data):
    parts, numbers = structure_data(raw_data)
    gear_ratios = []
    for part_location in parts.keys():
        neighbors = number_in_neighborhood(part_location, numbers)
        if len(neighbors) == 2:
            gear_ratios.append(prod(list(number_in_neighborhood(part_location, numbers))))
        
    return sum(gear_ratios)

# %%
print(f"Solution task 2: {solve2(raw_data)}")
assert solve2(raw_data) == 82818007

# %%
from timeit import timeit
n = 10000
results = timeit("solve2(raw_data)", number=n, setup="from __main__ import solve2", globals=globals())
print(f"Average time task 2: {(results/n) * 10**3} ms")
# Average time task 2: 3.4995615499996346 ms
# %%
