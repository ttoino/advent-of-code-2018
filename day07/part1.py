import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict
import heapq as hq

with open("input") as inf, open("part1.out", "w+") as outf:
    graph = defaultdict(set)

    for i in inf:
        a = i.split()
        graph[a[1]].add(a[7])

    def not_ready():
        return ft.reduce(op.or_, graph.values(), set())

    q = list(graph.keys() - not_ready())
    hq.heapify(q)

    result = ""
    while len(q) > 0:
        n = hq.heappop(q)
        result += n

        edges = graph[n]
        del graph[n]

        for o in edges:
            if o not in not_ready():
                hq.heappush(q, o)

    outf.write(result)
