import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def parse(l: list[int]) -> tuple[list[int], int]:
    children, entries, *l = l
    result = 0

    for i in range(children):
        l, s = parse(l)
        result += s

    return l[entries:], result + sum(l[:entries])


with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(str(parse([int(n) for n in inf.readline().strip().split()])[1]))
