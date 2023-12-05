

#%%

from dataclasses import dataclass
from enum import Enum
import re
from math import prod

#%%

raw_data = []
with open("input", "r") as f:
    for line in f:
        raw_data.append(line)

#%%


class Colors(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

@dataclass
class Turn():
    red: int = 0
    green: int = 0
    blue: int = 0

    def __str__(self) -> str:
        return f"R:{self.red} G:{self.green} B:{self.blue}\n"

@dataclass
class Game():
    id: int
    turns: list[Turn]

    def min_cubes(self) -> dict[Colors, int]:
        min_color = {
            Colors.RED: 0,
            Colors.GREEN: 0,
            Colors.BLUE: 0,
        }
        for turn in self.turns:
            min_color[Colors.RED] = max(min_color[Colors.RED], turn.red)
            min_color[Colors.GREEN] = max(min_color[Colors.GREEN], turn.green)
            min_color[Colors.BLUE] = max(min_color[Colors.BLUE], turn.blue)
        
        return min_color


    def __str__(self) -> str:
        out = f"Game ID: {self.id}\n"
        for idx, turn in enumerate(self.turns):
            out += f"\t{idx}: {str(turn)}"
        return out


#%%
# Task 1

def solve1(raw_data) -> list[int]:
    game_pattern = r"Game (\d+)"
    turn_pattern = r"(\d+) (red|green|blue),?"

    max_red = 12
    max_green = 13
    max_blue = 14

    possible_game_ids = []

    for line in raw_data:
        split = re.split(r": |; ", line)
        game_id = int(re.match(game_pattern, split[0]).group(1))
        turn_list = split[1:]

        #turns = []
        bad = False
        for idx, turn in enumerate(turn_list):
            counts = {
                Colors.RED: 0,
                Colors.GREEN: 0,
                Colors.BLUE: 0,
            }
            matches = re.findall(turn_pattern, turn)
            for number, color in matches:
                counts[color] = int(number)

            if counts[Colors.RED] > max_red or counts[Colors.GREEN] > max_green or counts[Colors.BLUE] > max_blue:
                bad = True
                #print(f"Game {game_id}: turn {idx} r: {counts['red']} g: {counts['green']} b: {counts['blue']}")
                break
            # turns.append(Turn(**counts))
        
        if bad:
            # print(f"Game {game_id} wasn't possible")
            continue

        # game = Game(id=game_id, turns=turns)
        # possible_games.append(game)
        possible_game_ids.append(game_id)
    return sum(possible_game_ids)
#%%
print(f"Solution 1: {solve1(raw_data)}")
assert solve1(raw_data) == 2348

#%%
from timeit import timeit
n = 10000
results = timeit("solve1(raw_data)", number=n, setup="from __main__ import solve1", globals=globals())
print(f"Average time task 1: {(results/n) * 10**3} ms")


#%% 
# Task 2

def solve2(raw_data):
    game_pattern = r"Game (\d+)"
    turn_pattern = r"(\d+) (red|green|blue),?"

    all_games: list[Game] = []
    for line in raw_data:
        split = re.split(r": |; ", line)
        game_id = int(re.match(game_pattern, split[0]).group(1))
        turn_list = split[1:]

        turns = []
        for turn in turn_list:
            counts = {
                Colors.RED: 0,
                Colors.GREEN: 0,
                Colors.BLUE: 0,
            }
            matches = re.findall(turn_pattern, turn)
            for number, color in matches:
                counts[color] = int(number)

            turns.append(Turn(**counts))
        
        all_games.append(Game(id=game_id, turns=turns))

    products = []
    for game in all_games:
        products.append(prod(game.min_cubes().values()))

    return sum(products)
# %%
print(f"Solution task 2: {solve2(raw_data)}")
assert solve2(raw_data) ==76008


# %%
from timeit import timeit
n = 10000
results = timeit("solve2(raw_data)", number=n, setup="from __main__ import solve2", globals=globals())
print(f"Average time task 2: {(results/n) * 10**3} ms")

# %%
