import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part1.out", "w+") as outf:
    pattern = re.compile(r"\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})] (?:Guard #(\d+) begins shift|(wakes up)|(falls asleep))")
    l = sorted(inf)
    c = Counter()
    d = defaultdict(Counter)
    id = -1
    start = -1

    for i in l:
        match pattern.match(i).groups():
            case [mins, None, None, "falls asleep"]:
                start = int(mins)
            case [mins, None, "wakes up", None]:
                for m in range(start, int(mins)):
                    c[id] += 1
                    d[id][m] += 1
            case [_, _id, None, None]:
                id = int(_id)

    id = c.most_common(1)[0][0]

    outf.write(str(d[id].most_common(1)[0][0] * id))
