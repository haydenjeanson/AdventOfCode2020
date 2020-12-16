import utilities

lines = utilities.get_lines('Day10/input.txt')
print(len(lines))

for i in range(len(lines)):
    lines[i] = int(lines[i])

adapters = lines.copy()
adapters.sort()
adapters.append(adapters[-1] + 3)
print(adapters)


def part1(adapters):
    differences = [0, 0, 0]

    current_jolts = 0
    for jolt_rating in adapters:
        differences[jolt_rating - current_jolts - 1] += 1
        current_jolts = jolt_rating

    print(differences)

    flag = differences[0] * differences[2]
    print(flag)


def part2():

    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []

        def add_child(self, child):
            self.children.append(child)

    def DFS(current):
        num_paths = 0

        if not current in visited:
            if current.value == end:
                num_paths = 1
            else:
                for child in current.children:
                    num_paths += DFS(child)
            visited.append(current)

        return num_paths

    head = Node(0)

    for value in adapters:
        if value <= 3:
            head.add_child(Node(value))
            print(value)
        else:
            print(value)
            break
    print(head.children[-1].value)

    def setupGraph(current):
        for child in current.children:
            start = adapters.index(child.value) + 1
            for value in adapters[start:]:
                if value - child.value <= 3:
                    child.add_child(Node(value))
                else:
                    break
            setupGraph(child)

    setupGraph(head)

    visited = []
    end = adapters[-1]

    print(DFS(head))


part1(adapters)
part2()
