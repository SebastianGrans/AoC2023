#%%
import re


#%%
raw_data = []

with open("input", "r") as f:
    for line in f:
        raw_data.append(line.rstrip()) 



#%%
def solve(raw_data: list[str]):
    first_digit_pattern = r"(\d)"
    last_digit_pattern = r"(\d)(?!.*\d)"
    data = []

    for line in raw_data:
        value = ""
        first = re.search(first_digit_pattern, line).group(1)
        last = re.search(last_digit_pattern, line).group(1)
        value = first + last
        data.append(int(value))

    return sum(data)

#$$
print(f"Solution: {solve(raw_data)}")
assert solve(raw_data) == 54667

#%%
from timeit import timeit
n = 10000
results = timeit("solve(raw_data)", number=n, setup="from __main__ import solve", globals=globals())
print(f"Average time task 1: {(results/n) * 10**3} ms")

# %% [markdown]
# Solution to task 2

str_to_int = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}


def to_int(string: str) -> str:
    if len(string) == 1:
        return string

    return str_to_int[string]

#%%
def solve2(raw_data) -> int:
    first_digit_pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
    last_digit_pattern = r"(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)"

    data = []

    for line in raw_data:
        value = ""
        first = re.search(first_digit_pattern, line).group(1)
        last = re.search(last_digit_pattern, line[::-1]).group(1)
        value = to_int(first) + to_int(last)
        value = to_int(first) + to_int(last)
        data.append(int(value))

    return sum(data)


#%%
print(f"Solution task 2: {solve2(raw_data)}")
assert solve2(raw_data) == 54203
# %%

from timeit import timeit
n = 10000
results = timeit("solve2(raw_data)", number=n, setup="from __main__ import solve2", globals=globals())
print(f"Average time task 2: {(results/n) * 10**3} ms")

# %%
