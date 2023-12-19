#%%

from dataclasses import dataclass, field
from typing import ClassVar
from collections import Counter
from itertools import combinations
import re
#%% 

raw_data = open("example_input").readlines()

#%%
@dataclass
class Onsen():
    PATTERN: ClassVar = re.compile(r"(#+)")
    string: str
    arrangement: list[int]
    slot_idxs: list[int] = field(init=False)
    known: int = field(init=False)
    available: int = field(init=False)
    n_perm: int = field(init=False)

    def __post_init__(self):
        self.slot_idxs = [idx for idx, el in enumerate(self.string) if el == "?"]
        self.known = Counter(self.string)["#"]
        self.available = sum(self.arrangement) - self.known
        #self.n_perm = self.find_perms()

    def validate_perm(self, string):
        matches = re.finditer(self.PATTERN, string)
        return [len(m.group(0)) for m in matches] == self.arrangement
    
    def find_perms(self) -> int:
        candidates = combinations(self.slot_idxs, self.available)
        
        valid_perms = []
        for candidate in candidates:
            string = list(self.string)
            for idx in candidate:
                string[idx] = "#"
            string = "".join(string)
            if self.validate_perm(string):
                valid_perms.append(string)

        return len(valid_perms)

# %%
onsens: list[Onsen] = []
for line in raw_data:
    string, arr = line.rstrip().split()
    arr = list(map(int, arr.split(",")))
    onsens.append(Onsen(string, arr))
# %%

total = 0
for onsen in onsens:
    total += onsen.n_perm

print(f"{total=}")

# %%
# task 2

onsens: list[Onsen] = []
for line in raw_data:
    string, arr = line.rstrip().split()
    arr = list(map(int, arr.split(",")))
    onsens.append(Onsen(((string + "?")*5)[:-1], arr*5))
# %%

total = 0
for onsen in onsens:
    total += onsen.n_perm

print(f"{total=}")
# %%

for onsen in onsens:
    print(onsen.string)
    print(onsen.arrangement)
# %%
