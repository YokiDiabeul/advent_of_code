from dataclasses import dataclass
from collections import Counter
from typing import List
from lib import common
import numpy


def get_values_between(v1, v2, multiplier):
    if v1 > v2:
        return [*range(v1, v2 - 1, -1)]

    if v1 < v2:
        return [*range(v1, v2 + 1)]

    return [v1] * multiplier


def get_intersections_count(coordinates_data, include_diagonal):
    lines = []


class Line:
    def __init__(self, line):
        (x1, y1), (x2, y2) = [tuple(int(i) for i in x_y.split(",")) for x_y in line.split("->")]
        self.x = (x1, y1)
        self.y = (x2, y2)
        self.x_dist = abs(x1 - x2)
        self.y_dist = abs(y1 - y2)

    def value_between(self):
        multiplier = max(self.x_dist, self.y_dist) + 1
        x_values = get_values_between(self.x[0], self.y[0], multiplier)
        y_values = get_values_between(self.x[1], self.y[1], multiplier)
        return [(x, y) for x, y in zip(x_values, y_values)]

    def is_diagonal(self) -> bool:
        return self.x_dist != 0 and self.y_dist != 0

    def __repr__(self) -> str:
        return f"{self.x} -> {self.y} ({self.x_dist}, {self.y_dist})"


def count_intersection(lines, diagonal=False):
    if diagonal:
        values = [line.value_between() for line in lines]
    else:
        values = [line.value_between() for line in lines if not line.is_diagonal()]
    count = Counter([i for n in values for i in n])
    return len([i for i in count.values() if i > 1])


def day_5():
    print("Day 5")
    lines = [Line(line) for line in common.load_str_inputs("5.txt")]
    print("Part 1:", count_intersection(lines, True))


if __name__ == "__main__":
    day_5()
