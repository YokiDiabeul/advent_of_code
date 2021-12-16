from dataclasses import dataclass
from typing import List
from lib import common


@dataclass
class Case:
    n: int
    c: bool = False


@dataclass
class Board:
    rows: List[List[Case]]

    def check(self, nb: int):
        for line in self.rows:
            for c in line:
                if c.n == nb:
                    c.c = True

    def get_success(self) -> bool:
        for line in self.rows:
            if sum([l.c for l in line]) == len(line):
                return True

        for i in range(len(self.rows[0])):
            if sum([l[i].c for l in self.rows]) == len(self.rows):
                return True

    def get_score(self, success):
        flat = [i for n in self.rows for i in n]
        res = sum([i.n for i in flat if not i.c])
        print(res)
        return res * success


def load_boards(lines: list) -> list:
    boards = []
    board = []
    for line in lines:
        if not line:
            boards.append(board)
            board = []
        else:
            board.append([Case(int(n)) for n in line.replace("  ", " ").split(" ")])
    boards.append(board)
    return boards


def get_winner(commands, boards):
    for n in commands:
        for b in boards:
            b.check(n)
            if b.get_success():
                return b.get_score(n)


def get_last_winner(commands, boards):
    success = 0
    for n in commands:
        for b in boards:
            b.check(n)
            if b.get_success():
                success += 1
                print(b.get_score(n))
            if success == len(boards):
                print(n)
                return b.get_score(n)


def day_4():
    print("Day 4")
    lines = common.load_str_inputs("4_test.txt")
    commands = [int(l) for l in lines.pop(0).split(",")]
    lines.pop(0)
    boards = [Board(b) for b in load_boards(lines)]
    score = get_winner(commands, boards)
    print(score)
    score = get_last_winner(commands, boards)
    print(score)


if __name__ == "__main__":
    day_4()
