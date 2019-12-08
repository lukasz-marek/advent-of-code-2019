import os
from typing import NewType, Tuple, List, Set

DATA_SOURCE_PATH: str = os.path.abspath(os.path.join(__file__, os.pardir,os.pardir, "resources", "day3.txt"))

Point = NewType("Point", Tuple[int, int])
Node = NewType("Node", str)

def get_intermediate_waypoints(current_position: Point, next_node: Node) -> List[Point]:
    direction, steps = next_node[0], int(next_node[1:])
    if direction == "U":
        return [(current_position[0], current_position[1] + step) for step in range(1, steps + 1)]
    elif direction == "D":
        return [(current_position[0], current_position[1] - step) for step in range(1, steps + 1)]
    elif direction == "L":
        return [(current_position[0] - step, current_position[1]) for step in range(1, steps + 1)]
    elif direction == "R":
        return [(current_position[0] + step, current_position[1]) for step in range(1, steps + 1)]

def get_all_waypoints(nodes: List[Node]) -> List[Point]:
    intermediate_points: List[Point] = [(0, 0)]
    for node in nodes:
        path = get_intermediate_waypoints(intermediate_points[-1], node)
        intermediate_points.extend(path)
    return intermediate_points

def get_collisions(path1: List[Node], path2: List[Node]) -> Set[Point]:
    waypoints1, waypoints2 = get_all_waypoints(path1), get_all_waypoints(path2)
    return set(waypoints1) & set(waypoints2)

def compute_distance_from_center(point: Point) -> int:
    return abs(point[0]) + abs(point[1])

def solve_part_1() -> int:
    path1: List[Node] = []
    path2: List[Node] = []

    def parse_line(line: str) -> List[Node]:
        return [item.strip() for item in line.split(",")]
    
    with open(DATA_SOURCE_PATH) as datasource:
        for line_number, content in enumerate(datasource):
            if(line_number) == 0:
                path1.extend(parse_line(content))
            elif line_number == 1:
                path2.extend(parse_line(content))

    colliding_points = get_collisions(path1, path2)
    distances = (compute_distance_from_center(intersection) for intersection in colliding_points)
    return min(distance for distance in distances if distance > 0)

def solve_part_2() -> int:
    path1: List[Node] = []
    path2: List[Node] = []

    def parse_line(line: str) -> List[Node]:
        return [item.strip() for item in line.split(",")]
    
    with open(DATA_SOURCE_PATH) as datasource:
        for line_number, content in enumerate(datasource):
            if(line_number) == 0:
                path1.extend(parse_line(content))
            elif line_number == 1:
                path2.extend(parse_line(content))

    colliding_points = get_collisions(path1, path2)
    distances = (compute_distance_from_center(intersection) for intersection in colliding_points)
    return min(distance for distance in distances if distance > 0)

if __name__ == "__main__":
    print(solve_part_1())

