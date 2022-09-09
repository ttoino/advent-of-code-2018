import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    l = inf.readline().split()
    player_count = int(l[0])
    max_n = int(l[6])

    circle = [0]
    current = 0
    players = [0 for _ in range(player_count)]

    for n, player in zip(range(1, max_n + 1), it.cycle(range(player_count))):
        if n % 23 == 0:
            current -= 7
            current %= len(circle)
            players[player] += n + circle.pop(current)
            continue

        current += 2
        current %= len(circle)
        circle.insert(current, n)

    outf.write(str(max(players)))
