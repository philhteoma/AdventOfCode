with open("puzzle12input.txt", "r") as file:
    puzzle_input = file.read()

puzzle_input_list = puzzle_input.split("\n")

supported_towers = [x.split(" -> ")[1].split(", ") for x in puzzle_input_list if len(x.split(" -> ")) == 2]
supported_towers_set = set([x for y in supported_towers for x in y])

supporting_towers = [x.split(" -> ")[0].split(" ")[0] for x in puzzle_input_list if "->" in x]
supporting_towers_set = set(supporting_towers)

print(supporting_towers_set - supported_towers_set)

# test = "fwft (72) -> ktlj, cntj, xhth"
#
# print("->" in test)

#print(supported_towers_set)
