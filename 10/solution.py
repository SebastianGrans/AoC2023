
#%%
raw_data = list(map(str.rstrip, open("example_input3").readlines()))
#raw_data = list(map(str.rstrip, open("input").readlines()))

#%%
bends_to_tuple = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}

compute_new_coordinate = lambda start, offset: (start[0] + offset[0], start[1] + offset[1])

#%%
points = {}
start = None
for ridx, line in enumerate(raw_data):
    for cidx, char in enumerate(line):
        try:
            offsets = bends_to_tuple[char]
            neighbors = list(map(lambda x: compute_new_coordinate((ridx, cidx), x), offsets))
            points[(ridx, cidx)] = {"neighbors": neighbors, "dist": 0}
        except KeyError:
            if char == "S":
                start = (ridx, cidx)
            continue
# %%



def connected_neighbors(starting_point: tuple[int, int], points_map) -> list[tuple[int, int]]:
    neighbor_offsets = [
        (-1, 0), # north
        (0, -1), # west
        (1, 0),  # south
        (0, 1), # east
    ]
    neighbors = []
    for neighbor_offset in neighbor_offsets:
        neighbor_coordinate = compute_new_coordinate(starting_point, neighbor_offset)
        try:
            neighbor_neighbors = points_map[neighbor_coordinate]["neighbors"]
            if starting_point in neighbor_neighbors:
                neighbors.append(neighbor_coordinate)
        except KeyError:
            continue
    
    return neighbors

# %%
start_neighbors = connected_neighbors(start, points)
points[start] = {"neighbors": start_neighbors, "dist": 0}

#%%

# %%
new_front = points[start]["neighbors"]
dist = 1

#reset dist
for point in points.values():
    point["dist"] = 0

while True:
    if not new_front:
        break
    front = new_front
    new_front = []
    for node in front:
        current_node = points[node]
        if current_node["dist"] > 0:
            # We came here before
            continue
        current_node["dist"] = dist
        new_front.extend(current_node["neighbors"])

    dist += 1


# %%
farthest_node = max(points.values(), key=lambda x: x["dist"])
print(f"Solution to task 1: {farthest_node['dist']}")
# %%

# DFS 

new_front = [points[start]["neighbors"][0]]
dist = 1

#reset dist
for point in points.values():
    point["dist"] = 0
points[start]["dist"] = -1
path = [start]
while True:
    if not new_front:
        break
    front = new_front
    new_front = []
    for node in front:
        current_node = points[node]
        if current_node["dist"] > 0:
            # We came here before
            continue
        if current_node["dist"] == -1:
            continue
        #     # looped
        #     new_front = []
        #     break
        current_node["dist"] = dist
        path.append(node)
        new_front.extend(current_node["neighbors"])

    dist += 1

# %%
