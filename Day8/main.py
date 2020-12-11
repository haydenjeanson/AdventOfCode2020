import utilities

lines = utilities.get_lines('Day8/input.txt')


# class Instruction():
#     def __init__(self, instruction_type, value):
#         self.type = instruction_type
#         self.value = value


def part1():
    visited = []
    i = 0
    counter = 0
    while i not in visited:
        visited.append(i)
        instruction = lines[i][:3]
        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            counter += int(lines[i][4:])
            i += 1
        elif instruction == 'jmp':
            i += int(lines[i][4:])
        else:
            print('invalid instruction. i: {} instruction: {}'.format(i, instruction))

    print(counter)


def part2():
    visited = []
    i = 0
    counter = 0
    changedLines = {}
    for j in range(len(lines)):
        changedLines[j] = []
    while i < len(lines):
        # print(lines)
        instruction = lines[i][: 3]

        if i in visited:
            if instruction == 'acc':
                counter += int(lines[i][4:])
                i += 1
                continue
            visited = []
            visited.append(i)
            if instruction == 'nop':
                if changedLines[i] != [] and not 'nop' in changedLines[i]:
                    lines[i] = 'jmp' + lines[i][3:]
                    changedLines[i].append('nop')

                elif len(changedLines[i]) == 2:
                    visited.pop()
                    i += 1

                elif changedLines[i] != [] and 'nop' in changedLines[i]:
                    i += 1

                else:
                    changedLines[i].append('nop')
                    lines[i] = 'jmp' + lines[i][3:]
                    i += int(lines[i][4:])

            elif instruction == 'jmp':
                if changedLines[i] != [] and not 'jmp' in changedLines[i]:
                    lines[i] = 'nop' + lines[i][3:]
                    changedLines[i].append('jmp')

                elif len(changedLines[i]) == 2:
                    visited.pop()
                    i += int(lines[i][4:])

                elif changedLines[i] != [] and 'jmp' in changedLines[i]:
                    i += int(lines[i][4:])
                else:
                    changedLines[i].append('jmp')
                    lines[i] = 'nop' + lines[i][3:]
                    i += 1

            else:
                print('invalid instruction. i: {} instruction: {}'.format(
                    i, instruction))
        else:
            visited.append(i)
            if instruction == 'nop':
                i += 1
            elif instruction == 'acc':
                counter += int(lines[i][4:])
                i += 1
            elif instruction == 'jmp':
                i += int(lines[i][4:])
            else:
                print('invalid instruction. i: {} instruction: {}'.format(
                    i, instruction))

    counter = 0
    i = 0
    while i < len(lines):
        instruction = lines[i][:3]
        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            counter += int(lines[i][4:])
            i += 1
        elif instruction == 'jmp':
            i += int(lines[i][4:])
        else:
            print('invalid instruction. i: {} instruction: {}'.format(i, instruction))

    print(counter)


part1()
part2()
