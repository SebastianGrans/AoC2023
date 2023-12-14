#%%
raw_data = [line.rstrip().split() for line in open("input").readlines()]

data = [list(map(int, line)) for line in raw_data]



#%%
tuple_diff = lambda x: x[0] - x[1]

new_values = []
for line in data:
    last_values = []
    current_line = line
    while True:
        if not any(current_line):
            # all zeros
            break
        
        last_values.append(current_line[-1])
        current_line = list(map(tuple_diff, zip(current_line[1:], current_line[:-1])))
        
    new_value = 0
    for val in last_values[::-1]:
        new_value = new_value + val

    new_values.append(new_value)



# %%
print(f"solution to task 1 {sum(new_values)}")
assert sum(new_values) == 1898776583
# %%


new_values = []
for line in data:
    first_values = []
    current_line = line
    while True:
        if not any(current_line):
            # all zeros
            break
        
        first_values.append(current_line[0])
        current_line = list(map(tuple_diff, zip(current_line[1:], current_line[:-1])))
        
    new_value = 0
    for val in first_values[::-1]:
        new_value = val - new_value

    new_values.append(new_value)

# %%
print(f"solution to task 2: {sum(new_values)}")
assert sum(new_values) == 1100



# %%
