import utilities

lines = utilities.get_lines('Day9/input.txt')

for i in range(len(lines)):
    lines[i] = int(lines[i])


def part1():
    line_number = 0
    unsorted = []
    while not len(unsorted) == 25:
        unsorted.append(lines[line_number])
        line_number += 1

    while line_number < len(lines):
        sorted25 = unsorted.copy()
        sorted25.sort()

        i = 0
        j = len(sorted25) - 1
        target = lines[line_number]
        while sorted25[i] + sorted25[j] != target and i < j:
            if sorted25[i] + sorted25[j] > target:
                j -= 1
            else:
                i += 1

        if i >= j:
            # target not found
            print(target)
            return target

        line_number += 1
        unsorted = unsorted[1:]
        unsorted.append(target)


def part2(target):
    start = 0
    end = 0
    current = lines[0]

    while current != target:
        if current < target:
            end += 1
            current += lines[end]
        else:
            current -= lines[start]
            start += 1

    print('Start: {}\nEnd: {}\nCurrent: {}'.format(start, end, current))
    subset = lines[start:end+1]
    subset.sort()

    flag = min(subset) + max(subset)
    print(flag)


target = part1()
part2(target)
