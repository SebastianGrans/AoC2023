# %%

import math


with open("input") as f:
    times = list(map(int, f.readline().rstrip().split()[1:]))
    distances = list(map(int, f.readline().rstrip().split()[1:]))

races = list(zip(times, distances))


# %%
# v = x (x in [0, t])
# tc = t - x
# d = v * tc = x * (t - x) > record distance
#
# d = xt - x^2
# => -x^2 + xt - d = 0
# a = -1
# b = t
# c = -d


def get_roots(time: int, d_rec: int):
    sqrt = math.sqrt(time**2 - 4 * d_rec)

    return ((-time - sqrt) / -2, (-time + sqrt) / -2)


# %%
charge_time = []
for time, d_rec in races:
    a, b = get_roots(time, d_rec)
    low = math.ceil(min(a, b))
    if low == min(a, b):
        low += 1
    charge_time.append(len(range(low, math.ceil(max(a, b)))))

# %%

time = int("".join(map(str, times)))
d_rec = int("".join(map(str, distances)))

# %%
a, b = get_roots(time, d_rec)
low = math.ceil(min(a, b))
if low == min(a, b):
    low += 1
charge_time.append(len(range(low, math.ceil(max(a, b)))))  # %%

# %%
