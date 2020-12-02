
import utilities


input_text = utilities.file_to_text('Day2/input.txt')
lines = input_text.split('\n')
lines.pop()


def part1():
    valid_count = 0
    for line in lines:
        line = line.split(':')
        amount, letter = line[0].split(' ')

        minimum, maximum = amount.split('-')
        minimum = int(minimum)
        maximum = int(maximum)

        l_count = 0
        for l in line[1]:
            if l == letter:
                l_count += 1

        if l_count >= minimum and l_count <= maximum:
            valid_count += 1

    print(valid_count)


def part2():
    valid_count = 0
    for line in lines:
        line = line.split(':')
        amount, letter = line[0].split(' ')

        minimum, maximum = amount.split('-')
        minimum = int(minimum)
        maximum = int(maximum)

        l_count = 0
        if line[1][minimum] == letter:
            l_count += 1

        if line[1][maximum] == letter:
            l_count += 1

        if l_count == 1:
            valid_count += 1

    print(valid_count)


part1()
part2()
