import utilities


def part1():
    for line1 in lines:
        line1 = int(line1)
        for line2 in lines:
            line2 = int(line2)
            if line1 + line2 == 2020:
                return(line1 * line2)

    return 'Failed'


def part2():
    for line1 in lines:
        line1 = int(line1)
        for line2 in lines:
            line2 = int(line2)
            for line3 in lines:
                line3 = int(line3)
                if line1 + line2 + line3 == 2020:
                    return(line1 * line2 * line3)

    return 'Failed'


input_text = utilities.file_to_text('Day1/input.txt')
lines = input_text.split('\n')
lines.pop()

print(part1())
print(part2())
