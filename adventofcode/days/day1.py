import os
from typing import Callable

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day1.txt"))

def calculate_required_fuel(mass: int) -> int:
    return (mass // 3)  - 2

def calculate_required_fuel_recursively(mass: int) -> int:
    required_fuel = 0
    while mass > 0:
        mass = calculate_required_fuel(mass)
        if mass > 0:
            required_fuel += mass
    return required_fuel

def solve(calculator: Callable[[int], int]) -> int:
    total_fuel_required: int  = 0
    with open(DATA_SOURCE_PATH) as data_source:
        for mass in data_source:
            mass = int(mass.strip())
            total_fuel_required += calculator(mass)
    return total_fuel_required

def solve_part_1() -> int:
    return solve(calculate_required_fuel)

def solve_part_2() -> int:
    return solve(calculate_required_fuel_recursively)

if __name__ == "__main__":
    print(solve_part_1())
    print(solve_part_2())