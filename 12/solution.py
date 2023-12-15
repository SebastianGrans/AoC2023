#%%

from dataclasses import dataclass
from enum import Enum

#%% 

raw_data = open("example_input").readlines()

#%%

class Condition(str, Enum):
    OPERATIONAL = "."
    DAMAGED = "#"
    UNKNOWN = "?"

@dataclass
class Onsen():
    


# %%
