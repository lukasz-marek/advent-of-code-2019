import os

def calculate_required_fuel(mass: int) -> int:
    return (mass // 3)  - 2

def solve() -> int:
    total_fuel_required = 0
    data_file = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day1.txt"))
    with open(data_file) as data_source:
        for mass in data_source:
            mass = int(mass.strip())
            total_fuel_required += calculate_required_fuel(mass)
    return total_fuel_required

if __name__ == "__main__":
    print(solve())