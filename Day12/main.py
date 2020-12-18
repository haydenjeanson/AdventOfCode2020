import utilities

lines = utilities.get_lines('Day12/input.txt')


def part1():
    # north = 0, east = 1, south = 2, west = 3. Start facing east.
    direction = 1

    # Set up vertical/horizontal values. Starts at (0,0)
    vertical = 0
    horizontal = 0

    # command_dict = {'N':, 'S':, 'E':, 'W':, 'L':, 'R':, 'F'}

    for line in lines:
        action, value = line[0], int(line[1:])

        if action == 'N':
            vertical += value

        elif action == 'S':
            vertical -= value

        elif action == 'E':
            horizontal += value

        elif action == 'W':
            horizontal -= value

        elif action == 'L':
            direction = (direction - value // 90) % 4

        elif action == 'R':
            direction = (direction + value // 90) % 4

        elif action == 'F':
            if direction == 0:
                vertical += value
            elif direction == 2:
                vertical -= value
            elif direction == 1:
                horizontal += value
            elif direction == 3:
                horizontal -= value

    # Calculate manhattan distance
    flag = abs(vertical) + abs(horizontal)
    print(flag)


def part2():
    # north = 0, east = 1, south = 2, west = 3. Start facing east.
    # direction = {0: 'north', 1: 'east', 2: 'south', 3: 'west'}

    # Set up vertical/horizontal values. Starts at (0,0)
    vertical = 0
    horizontal = 0
    w1 = [1, 0]
    w2 = [10, 1]

    # command_dict = {'N':, 'S':, 'E':, 'W':, 'L':, 'R':, 'F'}

    for line in lines:
        action, value = line[0], int(line[1:])

        if action == 'N':
            if w1[1] == 0:
                w1[0] += value
            elif w1[1] == 2:
                w1[0] -= value

            if w2[1] == 0:
                w2[0] += value
            elif w2[1] == 2:
                w2[0] -= value
        elif action == 'S':
            if w1[1] == 0:
                w1[0] -= value
            elif w1[1] == 2:
                w1[0] += value

            if w2[1] == 0:
                w2[0] -= value
            elif w2[1] == 2:
                w2[0] += value

        elif action == 'E':
            if w1[1] == 1:
                w1[0] += value
            elif w1[1] == 3:
                w1[0] -= value

            if w2[1] == 1:
                w2[0] += value
            elif w2[1] == 3:
                w2[0] -= value
        elif action == 'W':
            if w1[1] == 1:
                w1[0] -= value
            elif w1[1] == 3:
                w1[0] += value

            if w2[1] == 1:
                w2[0] -= value
            elif w2[1] == 3:
                w2[0] += value

        elif action == 'L':
            w1[1] = (w1[1] - value // 90) % 4
            w2[1] = (w2[1] - value // 90) % 4

        elif action == 'R':
            w1[1] = (w1[1] + value // 90) % 4
            w2[1] = (w2[1] + value // 90) % 4

        elif action == 'F':
            if w1[1] == 0:
                vertical += value * w1[0]
            elif w1[1] == 2:
                vertical -= value * w1[0]
            elif w1[1] == 1:
                horizontal += value * w1[0]
            else:
                horizontal -= value * w1[0]

            if w2[1] == 0:
                vertical += value * w2[0]
            elif w2[1] == 2:
                vertical -= value * w2[0]
            elif w2[1] == 1:
                horizontal += value * w2[0]
            else:
                horizontal -= value * w2[0]

    # Calculate manhattan distance
    flag = abs(vertical) + abs(horizontal)
    print(flag)


part1()
part2()
