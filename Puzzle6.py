class Grid:
    def __init__(self, puzzle_input):
        self.x = 5
        self.y = 5
        self.grid = self.build_grid()
        self.set_value(self.x, self.y, 1)
        self.facing = "east"
        self.facing_count = 0
        self.direction_list = ["east", "north", "west", "south"]
        self.puzzle_input = puzzle_input
        print("Class Grid Initiated")

    def build_grid(self):
        grid = []
        for i in range((self.x * 2) + 1):
            grid.append([0]*((self.x * 2) + 1))
        return grid

    def get_value(self, x, y):
        return self.grid[y][x]

    def set_value(self, x, y, value):
        self.grid[y][x] = value

    def step_forward(self):
        if self.facing == "east":
            self.x += 1
        if self.facing == "north":
            self.y += 1
        if self.facing == "west":
            self.x -= 1
        if self.facing == "south":
            self.y -= 1

    def look_left(self):
        if self.facing == "east":
            return(self.get_value(self.x, self.y + 1))
        if self.facing == "north":
            return(self.get_value(self.x - 1, self.y))
        if self.facing == "west":
            return(self.get_value(self.x, self.y -1))
        if self.facing == "south":
            return(self.get_value(self.x + 1, self.y))

    def sum_surounding_squares(self):
        x_val = [self.x-1, self.x, self.x+1]
        y_val = [self.y-1, self.y, self.y+1]

        coords_to_check = [[(x, y_val[0]), (x, y_val[1]), (x, y_val[2])] for x in x_val]
        coords_to_check = [x for y in coords_to_check for x in y]

        return sum([self.get_value(x, y) for x, y in coords_to_check])

    def progress(self):
        self.step_forward()
        print("Current Square: ({},{})".format(self.x, self.y))
        value = self.sum_surounding_squares()
        print("Sum Value: ", value)
        self.set_value(self.x, self.y, value)
        print("Look Left: ",self.look_left())
        if self.look_left() == 0:
            self.facing_count  = (self.facing_count + 1) % 4
            self.facing = self.direction_list[self.facing_count]
        return value

    def print_grid(self):
        for line in self.grid:
            for number in line:
                digits = len(str(number))
                pad = " " * (6 - digits)
                print(pad + str(number), end = " ")
            print("")

puzzle_input = 312051

puzzle_grid = Grid(puzzle_input)

puzzle_grid.print_grid()

while True:
    try:
        result = puzzle_grid.progress()
        print((puzzle_grid.x, puzzle_grid.y))
        puzzle_grid.print_grid()
        if result > puzzle_input:
            break
    except IndexError:
        break

final_value = result

print("Final Value: ", final_value)
