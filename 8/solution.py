#%%
import math
import re
#%%
raw_data = open("input").readlines()
directions = raw_data[0].rstrip()

#%%
pattern = re.compile(r"([\w]{3}) = \(([\w]{3}), ([\w]{3})\)")
node_map: dict[str, tuple[str, str]]= {}
for line in raw_data[2:]:
    match = re.match(pattern, line)
    node_map[match.group(1)] = (match.group(2), match.group(3))

#%%
dirmapping = {
    "R": 1,
    "L": 0
}
# %%

current_node = "AAA"
i = 0
while True:
    current_node = node_map[current_node][dirmapping[directions[i % len(directions)]]]
    i += 1
    # if next_node == current_node:
    #     raise RuntimeError
    # if i % 100_000 == 0:
    #     print(i)
    if current_node == "ZZZ":
        print(f"Reached goal in {i} steps")
        break

# %%

# Task 2

starting_nodes = {k: {"steps": [], "endnodes": []} for k in node_map.keys() if k[2] == "A"}
_ = [print(k) for k in starting_nodes]


#%%

for starting_node, snodedict in starting_nodes.items():
    i = 0
    steps = 0
    current_node = starting_node
    while True:
        next_node = node_map[current_node][dirmapping[directions[i % len(directions)]]]
        steps += 1
        i += 1
        if next_node[2] == "Z":
            snodedict["steps"].append(steps)
            steps = 0
            snodedict["endnodes"].append(next_node)
        current_node = next_node
        if len(snodedict["steps"]) > 4:
            break

#%%
_ = [print(f"{node}: {nodedict['steps'][0]}") for node, nodedict in starting_nodes.items()]

#%%
a = [node["steps"][0] for node in starting_nodes.values()]
#%%

print(f"solution to task 2: {math.lcm(*a)}")
# %%
