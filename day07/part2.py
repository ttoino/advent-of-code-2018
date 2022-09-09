import itertools as it
from time import sleep
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict
import heapq as hq

with open("input") as inf, open("part2.out", "w+") as outf:
    graph = defaultdict(set)

    for i in inf:
        a = i.split()
        graph[a[1]].add(a[7])

    def not_ready():
        return ft.reduce(op.or_, graph.values(), set())

    q = list(graph.keys() - not_ready())
    hq.heapify(q)
    visited = set()

    workers = [(None, 0) for _ in range(5)]

    for second in it.count():
        for i, (n, t) in enumerate(workers):
            if n is None:
                continue

            workers[i] = n, t + 1
            if t == 60 + ord(n) - ord('A'):
                edges = graph[n]
                del graph[n]

                for o in edges:
                    if o not in not_ready():
                        hq.heappush(q, o)

                workers[i] = (None, 0)

        free_workers = len([w for w in workers if w[0] is None])

        if free_workers == 5 and len(q) == 0:
            outf.write(str(second))
            break

        while len(q) > 0 and free_workers > 0:
            n = hq.heappop(q)

            for i, worker in enumerate(workers):
                if worker[0] is None:
                    workers[i] = (n, 0)
                    free_workers -= 1
                    break
