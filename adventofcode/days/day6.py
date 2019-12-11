import os
from typing import Dict, Optional, List, Set
from collections import defaultdict

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day6.txt"))


def count_object_orbits(orbitting: str, data: Dict[str, str]) -> int:
    to_visit: List[str] = [orbitting]
    orbits = 0
    while to_visit:
        current = to_visit.pop()
        orbitting = data.get(current, [])
        orbits += len(orbitting)
        to_visit.extend(orbitting)
    return orbits

def count_all_orbits(data: Dict[str, List[str]]) -> int:
    orbits = 0
    for core in data.keys():
        orbits += count_object_orbits(core, data)
    return orbits

def load_data() -> Dict[str, List[str]]:
    data = defaultdict(list)
    with open(DATA_SOURCE_PATH) as source:
        for line in source:
            line = line.strip()
            core, orbitting = line.split(")")
            data[core].append(orbitting)
    return data

def solve_part_1() -> int:
    data = load_data()
    return count_all_orbits(data)

if __name__ == "__main__":
    print(solve_part_1())