import utils

x0 = 2
y0 = 12

map_width = 15
map_height = 15

my_map = utils.generate_map(map_width, map_height)

utils.add_obstacle(my_map, 6, 5, 3, 4)

utils.print_map(my_map)

start_location = utils.Location()
start_location.x = x0
start_location.y = y0

locations = [start_location]
weight = 1
while len(locations) > 0:
    nextLocations = []
    for location in locations:
        utils.set_weight(my_map, location, weight)
        nextLocations += utils.get_neighbors(my_map, location)
    utils.print_map(my_map)
    locations = utils.get_zero_weight_unique_locations(my_map, nextLocations)
    weight += 1
    input("Press Enter to continue ...\n")

print()
utils.print_map(my_map)
