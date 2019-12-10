from typing import List, NewType, Optional, Tuple
import os

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day2.txt"))

Program = List[int]

class TerminationException(Exception):
    pass

def get_value(pointer: int, mode: int, program: Program) -> int:
    return program[pointer] if mode == 0 else pointer

def opcode_1(at: int, program: Program, modes: List[int]) -> int:
    arg_1, arg_2, to = zip(program[at+1:at+4], modes)
    program[to[0]] = get_value(*arg_1, program) + get_value(*arg_2, program)
    return at + 4

def opcode_2(at: int, program: Program, modes: List[int]) -> int:
    arg_1, arg_2, to = zip(program[at+1:at+4], modes)
    program[to[0]] = get_value(*arg_1, program) * get_value(*arg_2, program)
    return at + 4

def opcode_3(at: int, program: Program, args: List[int]) -> int:
    target = program[at + 1]
    program[target] = args[0]
    return at + 2

def opcode_4(at: int, program: Program, *_) -> int:
    source = program[at + 1]
    print("output: {}".format(program[source]))
    return at + 2

def opcode_5(at: int, program: Program, modes: List[int]) -> int:
    check_value, go_to = zip(program[at+1:at+3], modes)
    is_true = get_value(*check_value, program) != 0
    return get_value(*go_to, program) if is_true else at + 3

def opcode_6(at: int, program: Program, modes: List[int]) -> int:
    check_value, go_to = zip(program[at+1:at+3], modes)
    is_false = get_value(*check_value, program) == 0
    return get_value(*go_to, program) if is_false else at + 3

def opcode_7(at: int, program: Program, modes: List[int]) -> int:
    arg_1, arg_2, to = zip(program[at+1:at+4], modes)
    arg_1, arg_2  = get_value(*arg_1, program), get_value(*arg_2, program)
    program[to[0]] = 1 if arg_1 < arg_2 else 0
    return at + 4

def opcode_8(at: int, program: Program, modes: List[int]) -> int:
    arg_1, arg_2, to = zip(program[at+1:at+4], modes)
    arg_1, arg_2  = get_value(*arg_1, program), get_value(*arg_2, program)
    program[to[0]] = 1 if arg_1 == arg_2 else 0
    return at + 4

def opcode_99(at: int, program: Program, modes: List[int]) -> int:
    raise TerminationException

OPCODE_REGISTRY = {
    1: opcode_1,
    2: opcode_2,
    3: opcode_3,
    4: opcode_4,
    5: opcode_5,
    6: opcode_6,
    7: opcode_7,
    8: opcode_8, 
    99: opcode_99
}

def parse_opcode(opcode: int) -> Tuple[int, List[int]]:
    as_string = str(opcode)
    operation, modes = int(as_string[-2:]), [int(digit) for digit in as_string[:-2]]
    modes = (3 - len(modes)) * [0] + modes
    return operation, modes[::-1]

def run_program(program: Program, *_,program_input = 0) -> None:
    at = 0
    try:
        while True:
            opcode, modes = parse_opcode(program[at])
            modes = modes if opcode != 3 else [program_input]
            at = OPCODE_REGISTRY[opcode](at, program, modes)
    except TerminationException as e:
        return program[0]

def solve_part_1() -> int:
    with open(DATA_SOURCE_PATH) as program_data:
        program_source = program_data.read().replace('\n', '')
        program = [int(opcode.strip()) for opcode in program_source.split(",")]

    program[1] = 12
    program[2] = 2
    return run_program(program)

def solve_part_2() -> Optional[int]:
    with open(DATA_SOURCE_PATH) as program_data:
        program_source = program_data.read().replace('\n', '')
        program = [int(opcode.strip()) for opcode in program_source.split(",")]


    for noun in range(0, 99):
        for verb in range(0, 99):
            temporary_program = program[:]
            temporary_program[1] = noun
            temporary_program[2] = verb

            if run_program(temporary_program) == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    print(solve_part_1())
    print(solve_part_2())





