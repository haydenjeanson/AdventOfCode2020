
import utilities


lines = utilities.get_lines('Day3/input.txt')


def part1():
    end = len(lines)
    vert = 0
    hor = 0
    treeCount = 0
    lineLen = len(lines[0])

    while vert < end:
        if lines[vert][hor] == '#':
            treeCount += 1

        vert += 1
        hor += 3
        hor = hor % lineLen

    print(treeCount)
    pass


def part2(slope):
    end = len(lines)
    vert = 0
    hor = 0
    treeCount = 0
    lineLen = len(lines[0])

    while vert < end:
        if lines[vert][hor] == '#':
            treeCount += 1

        vert += slope[1]
        hor += slope[0]
        hor = hor % lineLen

    return(treeCount)


# part1()


trees = []
trees.append(part2([1, 1]))
trees.append(part2([3, 1]))
trees.append(part2([5, 1]))
trees.append(part2([7, 1]))
trees.append(part2([1, 2]))
count = 1
for tree in trees:
    count *= tree

print(count)
