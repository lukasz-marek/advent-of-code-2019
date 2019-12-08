from constraint import *

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

def within_range(*vals) -> bool:
    value = int("".join(str(val) for val in vals))
    return MIN_CODE_VALUE <= value <= MAX_CODE_VALUE

def build_problem() -> Problem:
    problem = Problem()
    for variable in VARIABLES:
        problem.addVariable(variable, range(10))

    problem.addConstraint(non_decreasing_digits, VARIABLES)
    problem.addConstraint(repeating_digits, VARIABLES)
    problem.addConstraint(within_range, VARIABLES)

    return problem

def solve() -> int:
    problem = build_problem()
    return len(problem.getSolutions())

if __name__ == "__main__":
    print(solve())
    