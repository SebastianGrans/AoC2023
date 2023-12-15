#%%

from collections import Counter


#%% 

mapp = list(map(str.rstrip, open("input").readlines()))

#%%



mappt = list(map("".join, zip(*mapp)))

#%%
def pm(mapp):
    for line in mapp:
        print("".join(line))


# %%
import re
pattern = r"([O|\.]*)(#|$)"

new_mapp = []
for line in mappt:
    new_line = ""
    for match in re.finditer(pattern, line):
        c = Counter(match.group(1))
        new_line += "O" * c['O'] + "." * c['.'] + match.group(2)
    new_mapp.append(new_line)

#%%
mapptt =  list(map("".join, zip(*new_mapp)))

height = len(mapptt)
load = 0
for idx, line in enumerate(mapptt):
    c = Counter(line)
    load += c["O"] * (height - idx)

print(f"Load is {load}")



# %%
