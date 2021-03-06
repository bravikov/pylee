"""
MIT License

Copyright (c) 2018 Dmitry Bravikov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Project site: https://github.com/bravikov/pylee

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
