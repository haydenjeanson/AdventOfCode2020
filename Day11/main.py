import utilities
from copy import deepcopy

lines = utilities.get_lines('Day11/input.txt')


def pad(matrix, pad_amount):
    num_r = len(lines)
    num_c = len(lines[0])

    new = utilities.new_matrix(
        num_r + (pad_amount * 2), num_c + (pad_amount * 2), '.')

    num_r += pad_amount * 2
    num_c += pad_amount * 2

    for r in range(pad_amount, num_r - pad_amount):
        for c in range(pad_amount, num_c - pad_amount):
            new[r][c] = lines[r-pad_amount][c-pad_amount]

    return new


def part1():
    def train(matrix):
        """
        Rules:
            If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            Otherwise, the seat's state does not change.
        """
        num_r = len(matrix)
        num_c = len(matrix[0])

        output = deepcopy(matrix)

        changes = 0
        for r in range(pad_amount, num_r - pad_amount):
            for c in range(pad_amount, num_c - pad_amount):
                if matrix[r][c] != '.':
                    # update adjacent seats (this method is inneficient, and it could be done dynamically;
                    # but this works so I'm sticking with it for now)
                    adjacent_seats = [
                        matrix[r-1][c-1], matrix[r-1][c], matrix[r-1][c+1],
                        matrix[r][c-1],                   matrix[r][c+1],
                        matrix[r+1][c-1], matrix[r+1][c], matrix[r+1][c+1]
                    ]

                    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                    if matrix[r][c] == 'L' and (not '#' in adjacent_seats):
                        output[r][c] = '#'
                        changes += 1

                    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                    elif matrix[r][c] == '#' and adjacent_seats.count('#') >= 4:
                        output[r][c] = 'L'
                        changes += 1
                    # Otherwise, the seat's state does not change.

        return changes, output

    pad_amount = 4
    matrix = deepcopy(pad(lines, pad_amount))

    changes = -1
    while changes != 0:
        changes, matrix = train(matrix)

    flag = 0
    for row in matrix:
        flag += row.count('#')
    print(flag)


def part2():
    def train(matrix):
        """
        Rules:
            If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
            Otherwise, the seat's state does not change.
        """
        num_r = len(matrix)
        num_c = len(matrix[0])

        output = deepcopy(matrix)

        changes = 0
        for r in range(pad_amount, num_r - pad_amount):
            for c in range(pad_amount, num_c - pad_amount):
                if matrix[r][c] != '.':
                    # update adjacent seats
                    adjacent_seats = ['', '', '', '', '', '', '', '']
                    # 0=(r-1,c-1)   1=(r-1,c)   2=(r-1,c+1)
                    # 3=(r,c-1)                 4=(r,c+1)
                    # 5=(r+1,c-1)   6=(r+1,c)   7=(r+1,c+1)

                    # 0
                    search_r = 1
                    search_c = 1
                    current = matrix[r-search_r][c-search_c]
                    while current == '.':
                        search_r += 1
                        search_c += 1
                        if r-search_r >= 0 and c-search_c >= 0:
                            current = matrix[r-search_r][c-search_c]
                        else:
                            break
                    adjacent_seats[0] = current

                    # 1
                    search_r = 1
                    current = matrix[r-search_r][c]
                    while current == '.':
                        search_r += 1
                        if r-search_r >= 0:
                            current = matrix[r-search_r][c]
                        else:
                            break
                    adjacent_seats[1] = current

                    # 2
                    search_r = 1
                    search_c = 1
                    current = matrix[r-search_r][c+search_c]
                    while current == '.':
                        search_r += 1
                        search_c += 1
                        if r-search_r >= 0 and c+search_c < num_c:
                            current = matrix[r-search_r][c+search_c]
                        else:
                            break
                    adjacent_seats[2] = current

                    # 3
                    search_c = 1
                    current = matrix[r][c-search_c]
                    while current == '.':
                        search_c += 1
                        if c-search_c >= 0:
                            current = matrix[r][c-search_c]
                        else:
                            break
                    adjacent_seats[3] = current

                    # 4
                    search_c = 1
                    current = matrix[r][c+search_c]
                    while current == '.':
                        search_c += 1
                        if c+search_c < num_c:
                            current = matrix[r][c+search_c]
                        else:
                            break
                    adjacent_seats[4] = current

                    # 5
                    search_r = 1
                    search_c = 1
                    current = matrix[r+search_r][c-search_c]
                    while current == '.':
                        search_r += 1
                        search_c += 1
                        if r+search_r < num_r and c-search_c >= 0:
                            current = matrix[r+search_r][c-search_c]
                        else:
                            break
                    adjacent_seats[5] = current

                    # 6
                    search_r = 1
                    current = matrix[r+search_r][c]
                    while current == '.':
                        search_r += 1
                        if r+search_r < num_r:
                            current = matrix[r+search_r][c]
                        else:
                            break
                    adjacent_seats[6] = current

                    # 7
                    search_r = 1
                    search_c = 1
                    current = matrix[r+search_r][c+search_c]
                    while current == '.':
                        search_r += 1
                        search_c += 1
                        if r+search_r < num_r and c+search_c < num_c:
                            current = matrix[r+search_r][c+search_c]
                        else:
                            break
                    adjacent_seats[7] = current

                    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                    if matrix[r][c] == 'L' and (not '#' in adjacent_seats):
                        output[r][c] = '#'
                        changes += 1

                    # If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
                    elif matrix[r][c] == '#' and adjacent_seats.count('#') >= 5:
                        output[r][c] = 'L'
                        changes += 1
                    # Otherwise, the seat's state does not change.

        return changes, output

    pad_amount = 4
    matrix = deepcopy(pad(lines, pad_amount))

    changes = -1
    while changes != 0:
        changes, matrix = train(matrix)

    flag = 0
    for row in matrix:
        flag += row.count('#')
    print(flag)


part1()
part2()
