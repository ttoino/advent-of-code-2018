import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    d = {}
    claims = set()

    for i in inf:
        m = pattern.match(i)
        claim = set(
            it.product(range(int(m[2]),
                             int(m[2]) + int(m[4])),
                       range(int(m[3]),
                             int(m[3]) + int(m[5]))))
        claims.add(m[1])

        for id, s in d.items():
            if len(s & claim) > 0:
                claims.discard(id)
                claims.discard(m[1])

        d[m[1]] = claim

    outf.write(next(iter(claims)))
