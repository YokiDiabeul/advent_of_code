from typing import List


def load_inputs(filename: str) -> list:
    with open(filename) as file:
        return file.readlines()


def load_int_inputs(filename: str) -> List[int]:
    return [int(line) for line in load_inputs(filename)]


def count_bigger_in_list(inputs: List[int]) -> int:
    return sum([inputs[i - 1] < inputs[i] for i in range(1, len(inputs))])


def day_1():
    print("Day 1")
    inputs = load_int_inputs("1.txt")
    # inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    print("Part 1:", count_bigger_in_list(inputs))

    new_inputs = [inputs[i - 2] + inputs[i - 1] + inputs[i] for i in range(2, len(inputs))]
    print("Part 2:", count_bigger_in_list(new_inputs))


if __name__ == "__main__":
    day_1()
