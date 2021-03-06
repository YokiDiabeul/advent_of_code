from typing import List
from lib import common


def count_in_list(inputs: List[str], i: int, c: str):
    return [int(n[i]) for n in inputs].count(c)


def rating(inputs, b):
    nl = inputs.copy()
    for i in range(len(inputs[0])):
        c = count_in_list(nl, i, b)
        bit = b if c == len(nl) / 2 else int(c > len(nl) / 2)
        nl = [n for n in nl if int(n[i]) == bit]
        if len(nl) == 1:
            break
    return int(nl[0], 2)


def day_3():
    print("Day 3")
    inputs = common.load_str_inputs("3.txt")
    # inputs = [
    #     "00100",
    #     "11110",
    #     "10110",
    #     "10111",
    #     "10101",
    #     "01111",
    #     "00111",
    #     "11100",
    #     "10000",
    #     "11001",
    #     "00010",
    #     "01010",
    # ]
    res = ""
    for i in range(len(inputs[0])):
        s = sum([int(n[i]) for n in inputs])
        res += "1" if s > len(inputs) / 2 else "0"

    r = ""
    for c in res:
        r += "0" if c == "1" else "1"

    gamma_rate = int(res, 2)
    print("gamma:", gamma_rate)
    epsilon_rate = int(r, 2)
    print("epsilon:", epsilon_rate)
    print("power:", gamma_rate * epsilon_rate)

    oxygen_generator_rating = rating(inputs, 1)
    co2_scrubber_rating = rating(inputs, 0)
    print(oxygen_generator_rating)
    print(co2_scrubber_rating)
    print(oxygen_generator_rating * co2_scrubber_rating)


if __name__ == "__main__":
    day_3()
