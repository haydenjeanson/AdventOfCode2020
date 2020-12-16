import utilities

lines = utilities.get_lines('Day10/input.txt')

for i in range(len(lines)):
    lines[i] = int(lines[i])


def part1():

    adapters = lines.copy()
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    differences = [0, 0, 0]

    current_jolts = 0
    for jolt_rating in adapters:
        differences[jolt_rating - current_jolts - 1] += 1
        current_jolts = jolt_rating

    print(differences)

    flag = differences[0] * differences[2]
    print(flag)


def part2():
    adapters = lines.copy()
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    paths = [1, 1, 1]
    for i in range(1, len(adapters)):
        parents = [adapters[i-3], adapters[i-2], adapters[i-1]]
        for j in range(3):
            if parents[j] < adapters[i] and adapters[i] - parents[j] <= 3:
                parents[j] = 1
            else:
                parents[j] = 0

        paths.append(paths[0]*parents[0] + paths[1] *
                     parents[1] + paths[2]*parents[2])
        paths = paths[1:]

    print(paths[-1])
    return paths[-1]


print('--- Part 1 ---')
part1()
print('--- Part 2 ---')
part2()
