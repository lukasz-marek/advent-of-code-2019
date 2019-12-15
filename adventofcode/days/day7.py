import os
from typing import NewType, Tuple, List, Set, Iterable
from itertools import permutations
from adventofcode.days.day2 import run_program

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day7.txt"))
Program = List[int]

def load_program() -> List[int]:
    program = []
    with open(DATA_SOURCE_PATH) as source:
        for line in source:
            program.extend(int(part.strip()) for part in line.strip().split(","))
    return program

def possible_settings() -> Iterable[List[int]]:
    for possible_solution in permutations(range(5)):
        yield list(possible_solution)

def generate_all_outputs(program: Program) -> Iterable[int]:
    for setting in possible_settings():
        previous_outputs = [0]

        for amplifier_setting in setting:
            program_inputs = [amplifier_setting] + previous_outputs
            _, previous_outputs = run_program(program[:], program_inputs=program_inputs)

        yield previous_outputs[-1]

def solve_part_1() -> int:
    program = load_program()
    return max(generate_all_outputs(program))

if __name__ == "__main__":
    print(solve_part_1())