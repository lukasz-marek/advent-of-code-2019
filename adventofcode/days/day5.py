from adventofcode.days.day2 import run_program

from typing import List, NewType, Optional, Tuple
import os

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day5.txt"))

Program = List[int]
def solve_part_1() -> int:
    with open(DATA_SOURCE_PATH) as program_data:
        program_source = program_data.read().replace('\n', '')
        program = [int(opcode.strip()) for opcode in program_source.split(",")]

    # program[1] = 12
    # program[2] = 2
    return run_program(program)

if __name__ == "__main__":
    print(solve_part_1())
