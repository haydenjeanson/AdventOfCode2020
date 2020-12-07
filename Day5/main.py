
import utilities
import math


lines = utilities.get_lines('Day5/input.txt')


def binary_search_modified(data, s, e, dir):
    m = math.floor((s + e) / 2)

    if dir == 'F' or dir == 'L':
        return data[s:m+1]
    else:
        return data[m+1:]


def part1():
    global lines
    max_id = -1

    for line in lines:
        rows = [i for i in range(128)]
        for dir in line[:7]:
            rows = binary_search_modified(rows, 0, len(rows)-1, dir)

        seat_id = rows[0] * 8

        cols = [i for i in range(8)]
        for dir in line[7:]:
            cols = binary_search_modified(cols, 0, len(cols)-1, dir)
        seat_id += cols[0]

        if seat_id > max_id:
            max_id = seat_id

    print(max_id)


def part2():
    global lines
    max_id = -1

    seats = [i for i in range(907)]

    for line in lines:
        rows = [i for i in range(128)]
        for dir in line[:7]:
            rows = binary_search_modified(rows, 0, len(rows)-1, dir)

        seat_id = rows[0] * 8

        cols = [i for i in range(8)]
        for dir in line[7:]:
            cols = binary_search_modified(cols, 0, len(cols)-1, dir)
        seat_id += cols[0]

        seats.remove(seat_id)

    i = 0
    for seat_num in seats:
        if seat_num != i:
            print(seat_num)
        i += 1

    print(seats)


part2()
