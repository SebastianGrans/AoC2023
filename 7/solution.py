
#%%
from dataclasses import dataclass, field
from enum import IntEnum, auto
from collections import Counter
#%%

#raw_data = open("example_input").readlines()
raw_data = open("input").readlines()

#%%

class HandType(IntEnum):
    HIGHCARD = auto() # 5 
    ONEPAIR = auto() # 4 1,1,1,2
    TWOPAIR = auto() # 3 1,2,2
    THREEOFAKIND = auto() # 3 1,1,3
    FULLHOUSE = auto() # 2 2, 3
    FOUROFAKIND = auto() # 2 1, 4
    FIVEOFAKIND = auto() # 1


@dataclass
class Hand():
    hand: str
    bid: str
    typ: HandType = field(init=False)
    value: int = field(init=False)

    def __post_init__(self):
        counter = Counter(self.hand)
        self.value = Hand.str_to_hex(self.hand)
        match len(counter):
            case 5:
                self.typ = HandType.HIGHCARD
            case 4:
                self.typ = HandType.ONEPAIR
            case 3:
                self.typ = self._three_kinds(counter)
            case 2:
                self.typ = self._two_kinds(counter)
            case 1:
                self.typ = HandType.FIVEOFAKIND
            case _:
                raise RuntimeError

    def _three_kinds(self, counter: Counter) -> HandType:
        match sorted(counter.values()):
            case [1, 2, 2]:
                return HandType.TWOPAIR
            case [1, 1, 3]:
                return HandType.THREEOFAKIND
            case _:
                raise RuntimeError 


    def _two_kinds(self, counter: Counter) -> HandType:
        match sorted(counter.values()):
            case [2, 3]:
                return HandType.FULLHOUSE
            case [1, 4]:
                return HandType.FOUROFAKIND
            case _:
                raise RuntimeError 
    
    @staticmethod
    def str_to_hex(string: str) -> int:
        s2h = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        value = 0
        for c in string:
            value <<= 4
            if c.isnumeric():
                value += int(c)
            else:
                value += s2h[c]
        
        return value

    def __str__(self):
        print(f"Hand: {self.hand} Bid: {self.bid} Type: {self.typ.name}")

#%%
hands_by_category = {handtype: [] for handtype in HandType}
for line in raw_data:
    hand_str, bid = line.rstrip().split()
    hand = Hand(hand_str, int(bid))
    hands_by_category[hand.typ].append(hand)

#%%
ranked_list = []
sortkey = lambda x: x.value
for hand_type in HandType:
    ranked_list += sorted(hands_by_category[hand_type], key=sortkey)

#%%
winnings = 0
for idx, hand in enumerate(ranked_list):
    winnings += (idx+1) * hand.bid

print(f"Solution to task 1: {winnings}")
assert winnings == 248422077

# %%
@dataclass
class Hand():
    hand: str
    bid: str
    typ: HandType = field(init=False)
    value: int = field(init=False)

    
    def __post_init__(self):
        counter = Counter(self.hand)
        self.value = Hand.str_to_hex(self.hand)
        match len(counter):
            case 5:
                if "J" in counter:
                    self.typ = HandType.ONEPAIR
                else:
                    self.typ = HandType.HIGHCARD
            case 4:
                if "J" in counter:
                    self.typ = HandType.THREEOFAKIND
                else:
                    self.typ = HandType.ONEPAIR
            case 3:
                self.typ = self._three_kinds(counter)
            case 2:
                if "J" in counter:
                    self.typ = HandType.FIVEOFAKIND
                else:
                    self.typ = self._two_kinds(counter)
            case 1:
                self.typ = HandType.FIVEOFAKIND
            case _:
                raise RuntimeError

    def _three_kinds(self, counter: Counter) -> HandType:
        match sorted(counter.values()):
            case [1, 2, 2]:
                if counter["J"] == 1:
                    return HandType.FULLHOUSE
                if counter["J"] == 2:
                    return HandType.FOUROFAKIND
                return HandType.TWOPAIR
            case [1, 1, 3]:
                if "J" in counter:
                    return HandType.FOUROFAKIND
                return HandType.THREEOFAKIND
            case _:
                raise RuntimeError 
    
    def _two_kinds(self, counter: Counter) -> HandType:
        match sorted(counter.values()):
            case [2, 3]:
                return HandType.FULLHOUSE
            case [1, 4]:
                return HandType.FOUROFAKIND
            case _:
                raise RuntimeError 
    
    @staticmethod
    def str_to_hex(string: str) -> int:
        s2h = {
            "T": 10,
            "J": 1,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        value = 0
        for c in string:
            value <<= 4
            if c.isnumeric():
                value += int(c)
            else:
                value += s2h[c]
        
        return value


# %%
hands_by_category = {handtype: [] for handtype in HandType}
for line in raw_data:
    hand_str, bid = line.rstrip().split()
    hand = Hand(hand_str, int(bid))
    hands_by_category[hand.typ].append(hand)

# %%

ranked_list = []
sortkey = lambda x: x.value
for hand_type in HandType:
    ranked_list += sorted(hands_by_category[hand_type], key=sortkey)

#%%
winnings = 0
for idx, hand in enumerate(ranked_list):
    winnings += (idx+1) * hand.bid

print(f"Solution to task 2: {winnings}")

# %%
