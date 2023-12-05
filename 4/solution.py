#%%
from dataclasses import dataclass, field
import re

#%% 
raw_data = []
with open("input", "r") as f:
    for line in f:
        raw_data.append(line)

#%%
@dataclass
class Card():
    id: int
    winning_numbers: set[int]
    numbers: set[int]
    instances: int = field(default=1)
    matches: set[int] = field(init=False)

    def __post_init__(self):
        self.matches = self.winning_numbers & self.numbers


#%% 

def structure_data(raw_data) -> list[Card]:
    cards: list[Card] = []
    for line in raw_data:
        _, id, winning, your_numbers = re.split("Card |: | \| ", line)
        winning = set(list(map(int, winning.split())))
        your_numbers = set(list(map(int, your_numbers.split())))
        cards.append(Card(int(id), winning, your_numbers))
    
    return cards
#%%

def solve1(raw_data) -> int:
    cards = structure_data(raw_data)

    points = 0
    for card in cards:
        if len(card.matches) > 0:
            points += 2**(len(card.matches) - 1)

    return points


# %%
print(f"Solution task 1: {solve1(raw_data)}")
assert solve1(raw_data) == 26346


#%%
from timeit import timeit
n = 10000
results = timeit("solve1(raw_data)", number=n, setup="from __main__ import solve1", globals=globals())
print(f"Average time task 1: {(results/n) * 10**3} ms")

# %%
# Task 2

def solve2(raw_data):
    cards = structure_data(raw_data)
    cards_dict = {card.id: card for card in cards}

    for card in cards:
        matches = len(card.matches)
        start = card.id + 1
        stop = start + matches
        for i in range(start, stop):
            cards_dict[i].instances += card.instances

    number_of_cards = 0
    for card in cards:
        number_of_cards += card.instances

    return number_of_cards

# %%
print(f"Solution task 2: {solve2(raw_data)}")
assert solve2(raw_data) == 8467762

# %%
from timeit import timeit
n = 10000
results = timeit("solve2(raw_data)", number=n, setup="from __main__ import solve2", globals=globals())
print(f"Average time task 2: {(results/n) * 10**3} ms")


# %%
