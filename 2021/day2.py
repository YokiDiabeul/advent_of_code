from typing import List
from lib import common


def day_2():
    print("Day 2")
    inputs = common.load_str_inputs("2.txt")
    # inputs = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    formated_inputs = [v.split(" ") for v in inputs]

    depth = 0
    position = 0
    aim = 0
    for value in formated_inputs:
        mov = value[0]
        val = int(value[1])
        if mov == "down":
            aim += val
        elif mov == "up":
            aim -= val
        elif mov == "forward":
            position += val
            depth += aim * val

    res = depth * position
    print(res)


if __name__ == "__main__":
    day_2()
