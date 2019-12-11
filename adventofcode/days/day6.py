import os
from typing import Dict, Optional, List, Set
from collections import defaultdict

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day6.txt"))

def find_path_to_absolute_core(source: str, data: Dict[str, str]) -> List[str]:
    path = []
    current = source
    while current:
        path.append(current)
        current = data.get(current, None)
    return path


def find_shortest_path(source: str, destination: str, data: Dict[str, List[str]]) -> List[List[str]]:
    connections = {}
    for core, orbitees in data.items():
        for orbitee in orbitees:
            connections[orbitee] = core
    path_prefix = find_path_to_absolute_core(source, connections)
    path_suffix = find_path_to_absolute_core(destination, connections)[::-1]

    prefix_copy = path_prefix[:]

    while len(set(path_prefix) & set(path_suffix)) > 1:
        del path_prefix[-1]

    while len(set(prefix_copy) & set(path_suffix)) > 1:
        del path_suffix[0]

    del path_prefix[-1]

    return path_prefix + path_suffix

def count_object_orbits(orbitting: str, data: Dict[str, List[str]]) -> int:
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

def solve_part_2() -> int:
    data = load_data()
    return len(find_shortest_path("YOU", "SAN", data)) - 3

if __name__ == "__main__":
    print(solve_part_1())
    print(solve_part_2())