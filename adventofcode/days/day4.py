from constraint import *
from typing import List

DIGITS_IN_CODE = 6
VARIABLES = ["digit_{}".format(i) for i in range(DIGITS_IN_CODE)]
MIN_CODE_VALUE = 240920
MAX_CODE_VALUE = 789857

def non_decreasing_digits(*vals) -> bool:
    for i in range(len(vals) - 1):
        if vals[i] > vals[i + 1]:
            return False
    return True

def repeating_digits(*vals) -> bool:
    for i in range(len(vals) - 1):
        if vals[i] == vals[i + 1]:
            return True
    return False

def repeating_exactly_2_digits(*vals) -> bool:
    def partition(items: List[int]) -> List[List[int]]:
        parts = {}
        jump = 0
        for position in range(len(items)):
            if jump > 0:
                jump -=1
                continue
            parts[position] = [items[position]]
            for metaposition in range(position + 1, len(items)):
                if items[position] == items[metaposition]:
                    parts[position].append(items[metaposition])
                    jump += 1
                else:
                    break
        return list(parts.values())

    return any(len(part) == 2 for part in partition(vals))


def within_range(*vals) -> bool:
    value = int("".join(str(val) for val in vals))
    return MIN_CODE_VALUE <= value <= MAX_CODE_VALUE

def build_problem(*constraints) -> Problem:
    problem = Problem()
    for variable in VARIABLES:
        problem.addVariable(variable, range(10))

    for constraint in constraints:
        problem.addConstraint(constraint, VARIABLES)

    return problem

def solve_part_1() -> int:
    problem = build_problem(non_decreasing_digits, repeating_digits, within_range)
    return len(problem.getSolutions())

def solve_part_2() -> int:
    problem = build_problem(non_decreasing_digits, repeating_exactly_2_digits, within_range)
    return len(problem.getSolutions())


if __name__ == "__main__":
    print(solve_part_1())
    print(solve_part_2())
