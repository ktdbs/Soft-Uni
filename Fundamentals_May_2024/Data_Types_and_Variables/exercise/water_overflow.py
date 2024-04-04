num_of_lines = int(input())
space_left = 255
litter_in_tank = 0
for _ in range(num_of_lines):
    lines_of_water = int(input())

    if lines_of_water <=space_left:
        litter_in_tank +=lines_of_water
        space_left -= lines_of_water
    elif lines_of_water > space_left:
        print('Insufficient capacity!')


print(litter_in_tank)


