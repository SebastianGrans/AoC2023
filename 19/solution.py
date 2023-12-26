# %%

import re
import operator
from typing import Callable

# %%

raw_data = list(map(str.rstrip, open("input").readlines()))


# %%


class Rule:
    _pattern = re.compile(r"(x|m|a|s)(<|>)(\d+):(\w+)|(\w+)")

    key: str | None
    op: Callable | None
    value: int
    next_wf: str

    def __init__(self, next_wf: str, key: str | None = None, op: str | None = None, value: str | None = None) -> None:
        self.key = key
        self.value = int(value) if value else 0
        self.next_wf = next_wf

        if op == ">":
            self.op = operator.gt
        elif op == "<":
            self.op = operator.lt

    @classmethod
    def parse_rule(cls, rule: str) -> "Rule":
        res = re.search(cls._pattern, rule)
        assert res, "No match?"

        if res.group(5):
            return Rule(next_wf=res.group(5))
        else:
            key = res.group(1)
            op = res.group(2)
            value = res.group(3)
            next_wf = res.group(4)
            return Rule(next_wf, key, op, value)

    def apply(self, rankings: dict[str, int]) -> str:
        if self.key is None:
            return self.next_wf

        assert self.op is not None
        if self.op(rankings[self.key], self.value):
            return self.next_wf
        else:
            return ""


class Workflow:
    name: str
    rules: list[Rule]

    def __init__(self, workflow: str) -> None:
        self.rules = []

        name, rules = workflow.split("{")
        self.name = name

        rules = rules[:-1].split(",")
        for rule in rules:
            self.rules.append(Rule.parse_rule(rule))

    def apply(self, part_ranking: dict[str, int]) -> str:
        for rule in self.rules:
            ret = rule.apply(part_ranking)
            if ret:
                return ret
        else:
            assert False, "What?"


# %%
pattern = re.compile(r"(\d+)")


def str_rank_to_dict(ranking: str) -> dict[str, int]:
    matches = re.findall(pattern, ranking)
    assert len(matches) == 4
    return dict(zip(["x", "m", "a", "s"], map(int, matches)))


# %%
workflows: dict[str, Workflow] = {}
part_rankings: list[dict[str, int]] = []
wfs = True
for line in raw_data:
    if not line:
        wfs = False
        continue
    if wfs:
        wf = Workflow(line)
        workflows[wf.name] = wf
    else:
        part_rankings.append(str_rank_to_dict(line))


# %%
accepted_idxs = []
accepted = 0
rejected = 0
rank = part_rankings[0]

for idx, rank in enumerate(part_rankings):
    wf_key = "in"
    print(f"{wf_key} -->", end=" ")
    while True:
        next_wf = workflows[wf_key].apply(rank)
        if next_wf == "R":
            rejected += 1
        elif next_wf == "A":
            accepted_idxs.append(idx)
            accepted += 1
        else:
            wf_key = next_wf
            print(f"{wf_key} -->", end=" ")
            continue

        print(f"{next_wf}", end=" ")
        break

    print("")
# %%
summ = 0
for idx in accepted_idxs:
    summ += sum(part_rankings[idx].values())
# %%
