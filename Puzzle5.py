"""
 1 : 0
 2 : 1
 3 : 2
 4 : 1
 5 : 2
 6 : 1
 7 : 2
 8 : 1
 9 : 2
10 : 3
11 : 2
12 : 3
13 : 4
14 : 3
15 : 2
16 : 3
17 : 4
18 : 3
19 : 2
20 : 3
21 : 4
22 : 3
23 : 2
24 : 3
25 : 4
26 : 5

1
2 - 9
10 - 25
"""

from math import sqrt

puzzle_input = 312051

box_sizes = (x**2 for x in range(1000) if x % 2 == 1)

def find_input_box_size(puzzle_input):
    count = 0
    while True:
        square = next(box_sizes)
        if square > puzzle_input - 1:
            return(sqrt(square)), count
        count += 1

def find_corners(box_size):
    number_to_add = box_size - 1
    previous_box_finish = (box_size - 2)**2
    corner_0 = previous_box_finish
    corner_1 = corner_0 + number_to_add
    corner_2 = corner_1 + number_to_add
    corner_3 = corner_2 + number_to_add
    corner_4 = corner_3 + number_to_add
    return [corner_0, corner_1, corner_2, corner_3, corner_4]

def find_distance_from_corner(puzzle_input, corners):
    distances = [abs(x - puzzle_input) for x in corners]
    distance_from_corner = min(distances)
    return distance_from_corner

box_size, count = find_input_box_size(puzzle_input)
corners = find_corners(box_size)
distance_from_corner = find_distance_from_corner(puzzle_input, corners)
max_distance = count * 2
distance = max_distance - distance_from_corner

print(distance)
