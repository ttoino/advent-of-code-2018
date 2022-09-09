import itertools as it
from typing_extensions import Self
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


class CircularList():

    def __init__(self):
        self.current = None

    def insert(self, value):
        if self.current == None:
            self.current = self.Node(value)
        else:
            next = self.current.next
            new_node = self.Node(value, self.current, next)
            self.current.next = new_node
            next.prev = new_node
            self.current = new_node

    def pop(self):
        current = self.current
        self.current = current.next
        current.prev.next = self.current
        return current.value

    def skip_clockwise(self, n: int):
        for _ in range(n):
            self.current = self.current.next

    def skip_counterclockwise(self, n: int):
        for _ in range(n):
            self.current = self.current.prev

    class Node():

        def __init__(self, value, prev: Self = None, next: Self = None):
            self.value = value
            self.prev = prev or self
            self.next = next or self


with open("input") as inf, open("part2.out", "w+") as outf:
    l = inf.readline().split()
    player_count = int(l[0])
    max_n = int(l[6]) * 100

    circle = CircularList()
    circle.insert(0)
    players = [0 for _ in range(player_count)]

    for n, player in zip(range(1, max_n + 1), it.cycle(range(player_count))):
        if n % 23 == 0:
            circle.skip_counterclockwise(7)
            players[player] += n + circle.pop()
            continue

        circle.skip_clockwise(1)
        circle.insert(n)

    outf.write(str(max(players)))
