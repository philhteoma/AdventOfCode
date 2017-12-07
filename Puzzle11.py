puzzle_input = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
#puzzle_input = [0, 2, 7, 0]

iteration_list = [
    tuple(puzzle_input)
    ]

count = 0
while True:
    count += 1
    length_of_list = len(puzzle_input)

    max_number = max(puzzle_input)
    index_of_max = puzzle_input.index(max_number)

    puzzle_input[index_of_max] = 0

    excess = max_number % length_of_list
    even_distribution = int((max_number - excess) /  length_of_list)

    puzzle_input = [x + even_distribution for x in puzzle_input]

    indexes_to_modify = [ (x + index_of_max + 1) % length_of_list for x in range(excess)]

    for index in indexes_to_modify:
        puzzle_input[index] += 1

    tuple_to_add = tuple(puzzle_input)

    if tuple_to_add in iteration_list:
        print(tuple_to_add)
        print(count)
        break

    iteration_list.append(tuple_to_add)
print(len(iteration_list) - iteration_list.index(tuple_to_add))
