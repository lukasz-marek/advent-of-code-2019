from typing import List, NewType
import os

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day2.txt"))

Program = List[int]

class TerminationException(Exception):
    pass

def opcode_1(at: int, program: Program) -> None:
    arg_1, arg_2, to = program[at+1:at+4]
    program[to] = program[arg_1] + program[arg_2]

def opcode_2(at: int, program: Program) -> None:
    arg_1, arg_2, to = program[at+1:at+4]
    program[to] = program[arg_1] * program[arg_2]

def opcode_99(at: int, program: Program) -> None:
    raise TerminationException

def next_opcode(at: int) -> int:
    return at + 4

OPCODE_REGISTRY = {
    1: opcode_1,
    2: opcode_2,
    99: opcode_99
}

def run_program(program: Program) -> None:
    at = 0
    try:
        while True:
            OPCODE_REGISTRY[program[at]](at, program)
            at = next_opcode(at)
    except TerminationException as e:
        return program[0]

def solve_part_1() -> int:
    with open(DATA_SOURCE_PATH) as program_data:
        program_source = program_data.read().replace('\n', '')
        program = [int(opcode.strip()) for opcode in program_source.split(",")]

    program[1] = 12
    program[2] = 2
    return run_program(program)


if __name__ == "__main__":
    print(solve_part_1())




