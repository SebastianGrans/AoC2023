# %%

from collections import deque
from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.style.use("dark_background")
for k, v in mpl.rcParams.items():
    if "color" in k and v == "black":
        mpl.rcParams[k] = "#313a3f"


raw_data = list(map(str.split, map(str.rstrip, open("input").readlines())))
# raw_data = list(map(str.rstrip, open("input").readlines()))


# %%


@dataclass
class Trench:
    start: tuple[int, int]
    end: tuple[int, int]
    color: str
    color_int: tuple[int, int, int] = field(init=False)

    def __post_init__(self) -> None:
        r = int(self.color[1:3], base=16)
        g = int(self.color[3:5], base=16)
        b = int(self.color[5:7], base=16)
        self.color_int = (r, g, b)


dirr_map = {
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0),
    "U": (0, 1),
}

# %%
holes: list[Trench] = []


# %%
def new_coord(curr: tuple[int, int], direction: tuple[int, int], magnitude: int) -> tuple[int, int]:
    return (curr[0] + magnitude * direction[0], curr[1] + magnitude * direction[1])


# %%
start = (0, 0)
for dirr, length, color in raw_data:
    offset = dirr_map[dirr]
    color = color[1:-1]
    end = new_coord(curr=start, direction=offset, magnitude=int(length))
    holes.append(Trench(start=start, end=end, color=color))
    start = end

# %%

x_range = [10**8, -(10**8)]
y_range = [10**8, -(10**8)]
for trench in holes:
    x_range = [min([x_range[0], trench.start[0], trench.end[0]]), max([x_range[1], trench.start[0], trench.end[0]])]
    y_range = [min([y_range[0], trench.start[1], trench.end[1]]), max([y_range[1], trench.start[1], trench.end[1]])]

# %%
for trench in holes:
    trench.start = (trench.start[0] - x_range[0], trench.start[1] - y_range[0])
    trench.end = (trench.end[0] - x_range[0], trench.end[1] - y_range[0])

# %%

mapp = np.zeros(shape=(x_range[1] - x_range[0] + 1, y_range[1] - y_range[0] + 1)).astype(dtype=bool)
for trench in holes:
    xs = min(trench.start[0], trench.end[0])
    xe = max(trench.start[0], trench.end[0])
    ys = min(trench.start[1], trench.end[1])
    ye = max(trench.start[1], trench.end[1])
    mapp[xs : xe + 1, ys : ye + 1] = True


# %%
# bfs filling


def neighbors(coord):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    return [(coord[0] + x, coord[1] + y) for x, y in offsets]


# %%
# this feels like cheating
queue = deque([(100, 120)])
i = 0
while queue:
    current = queue.popleft()
    if mapp[current]:
        continue
    mapp[current] = True
    i += 1
    if i % 10000 == 0:
        plt.imshow(mapp)
        plt.show(block=False)
    queue.extend(neighbors(current))

plt.imshow(mapp)
plt.show(block=False)
# %%
print(mapp.sum())

# %%
