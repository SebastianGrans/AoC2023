#%%
from collections import OrderedDict
import re

#%%

# raw_data = open("example_input").readline().split(",")
raw_data = open("input").readline().rstrip().split(",")

#%%
values = []
for line in raw_data:
    value=0
    for char in line:
        value += ord(char)
        value *= 17
        _, value = divmod(value, 256)
    values.append(value)

print(f"solution to task 1 {sum(values)}")
# %%
def get_hash(line):
    value = 0
    for char in line:
        value += ord(char)
        value *= 17
        _, value = divmod(value, 256)

    return value
#%%

pattern = r"([a-z]+)(=|-)(\d|$)"

boxes = {k: OrderedDict() for k in range(256)}

for line in raw_data:
    match = re.match(pattern, line)
    box_id = get_hash(match.group(1))
    if match.group(2) == "=":
        boxes[box_id].update({match.group(1): match.group(3)})
    elif match.group(2) == "-":
        try:
            del boxes[box_id][match.group(1)]
        except KeyError:
            continue
    
# for box, values in boxes.items():
#     if len(values):
#         print(f"{box} {values}")
#     print("")

#%%
focusing_powers = []
for box, dictt in boxes.items():
    for slot, focal_length in enumerate(dictt.values()):
        focusing_power = (box + 1) * (slot+1) * (int(focal_length))
        focusing_powers.append(focusing_power)
        #print(f"{box=} {focal_length=} {slot=} => {focusing_power}")



# %%
