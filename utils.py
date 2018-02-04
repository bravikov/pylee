import copy


def print_map(my_map):
    for row in my_map:
        for cell in row:
            print("{:3}".format(cell), end=' ')
        print()
    print()


def generate_map(width, height):
    my_map = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        my_map.append(row)
    return my_map


def add_obstacle(my_map, x0, y0, width, heigth):
    for y in range(y0, y0 + heigth):
        for x in range(x0, x0 + width):
            if position_exists(my_map, x, y):
                my_map[y][x] = -1


class Location:
    x = 0
    y = 0

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def position_exists(my_map, x, y):
    location = Location()
    location.x = x
    location.y = y
    return location_exists(my_map, location)


def location_exists(my_map, location):
    if location.y < 0:
        return False
    if location.x < 0:
        return False
    if location.y >= len(my_map):
        return False
    if location.x >= len(my_map[location.y]):
        return False
    return True


def set_weight(my_map, location, weight):
    if location_exists(my_map, location):
        if my_map[location.y][location.x] > 0:
            return
        my_map[location.y][location.x] = weight


def get_zero_weight_unique_locations(my_map, locations):
    unique_locations = set()
    for location in locations:
        if my_map[location.y][location.x] == 0:
            unique_locations.add(location)

    return unique_locations


def get_neighbors(my_map, location):
    neighbors = []

    if not location_exists(my_map, location):
        return neighbors

    top = copy.copy(location)
    top.y += 1
    if location_exists(my_map, top):
        neighbors.append(top)

    bottom = copy.copy(location)
    bottom.y -= 1
    if location_exists(my_map, bottom):
        neighbors.append(bottom)

    rigth = copy.copy(location)
    rigth.x += 1
    if location_exists(my_map, rigth):
        neighbors.append(rigth)

    left = copy.copy(location)
    left.x -= 1
    if location_exists(my_map, left):
        neighbors.append(left)

    return neighbors
