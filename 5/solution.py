#%%

import re


#%%
#raw_data = open("input").readlines()
raw_data = open("example_input").readlines()
#%% 

_, seeds = re.split(": ", raw_data[0])
seeds = list(map(int, seeds.split()))

header_pattern = r"(\w+-to-\w+)"

mapping = {}

headers = []
header = True
for line in raw_data[2:]:
    if line == "\n":
        header = True
        continue
    
    if header:
        match = re.match(header_pattern, line)
        mapping[match.group(1)] = []
        headers.append(match.group(1))
        header = False
        continue
    
    dest_start, src_start, rangee = list(map(int, line.split()))
    mapping[headers[-1]].append((range(src_start, src_start+rangee), dest_start-src_start))

# %%
def thing_to_thing(map_list, number) -> int:
    for rangee, offset in map_list:
        if number in rangee:
            return number + offset
    return number

# %%

lowest_location = 9999999999999999
for seed in seeds:
    value = seed
    for map_name in headers:
        value = thing_to_thing(mapping[map_name], value)
        
    lowest_location = min(value, lowest_location)

# %%
print(f"Solution to task 1: {lowest_location}")
# %%

exit(0)

seed_ranges = []
for idx in range(0, len(seeds), 2):
    seed_ranges.append(range(seeds[idx], seeds[idx]+seeds[idx+1]))

seed_ranges = sorted(seed_ranges, key=lambda x: x.start, reverse=True)
# %%

#%%

def condense_range(ranges: list[range]) -> list[range]:
    new_ranges = []
    while ranges:
        rangee = ranges.pop()
        while ranges:
            next_range = ranges[0] 
            start_in = next_range.start in rangee
            if not start_in:
                # no overlap
                new_ranges.append(rangee)
                break
            
            rangee = range(rangee.start, max(rangee.stop, next_range.stop))
            new_ranges.append(rangee)
            ranges.pop()
            continue
    
    return new_ranges

#%%

seed_ranges = condense_range(seed_ranges)

#%%
def condense_range2(ranges: list[range]) -> list[range]:
    new_ranges = []
    while ranges:
        rangee = ranges.pop()
        while ranges:
            next_range = ranges[0] 
            start_in = next_range[0].start in rangee[0]
            if not start_in:
                # no overlap
                new_ranges.append(rangee)
                break
            
            rangee[0] = range(rangee[0].start, max(rangee[0].stop, next_range[0].stop))
            new_ranges.append(rangee)
            ranges.pop()
            continue
    
    return new_ranges

#%%
for keyy, ranges in mapping.items():
    mapping[keyy] = sorted(ranges, key=lambda x: x[0].start, reverse=True)


# %%

for map_name in headers:
    mapp = mapping[map_name]
    for idx in range(len(mapp) - 1):
        print(mapp[idx][0].start in mapp[idx][0])
# %%


# %%