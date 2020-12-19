import utilities

lines = utilities.get_lines('Day13/input.txt')


def part1():
    start_time = int(lines[0])
    bus_numbers = lines[1].split(',')

    first_bus = 0
    min_minutes = -1
    for bus in bus_numbers:
        if not bus.isalpha():
            bus = int(bus)
            minutes_to_wait = -1 * (start_time % -bus)
            if minutes_to_wait < min_minutes or min_minutes == -1:
                first_bus = bus
                min_minutes = minutes_to_wait

    flag = first_bus * min_minutes
    print(flag)


def part2():
    bus_numbers = lines[1].split(',')
    # bus_numbers[0] = int(bus_numbers[0])
    # first_with_0 = [0]
    # for i in range(1, len(bus_numbers)):
    #     if not bus_numbers[i].isalpha():
    #         bus_numbers[i] = int(bus_numbers[i])
    #         count = 1
    #         y = -1
    #         while y % bus_numbers[0] != 0:
    #             y = bus_numbers[i] * count - i
    #             count += 1

    #         first_with_0.append(y)
    #     else:
    #         first_with_0.append(-1)

    LCM = int(bus_numbers[0])
    times = [int(bus_numbers[0])]
    for i in range(1, len(bus_numbers)):
        if bus_numbers[i].isnumeric():
            while (times[0]+i) % int(bus_numbers[i]) != 0:
                for j in range(len(times)):
                    times[j] += LCM

            times.append(times[0] + i)

            LCM = 1
            for bus in bus_numbers[:i+1]:
                if bus.isnumeric():
                    # Since all input is prime
                    LCM *= int(bus)

    flag = times[0]
    print(flag)

    # max_location = first_with_0.index(max(first_with_0))
    # found = False
    # while not found:
    #     for i in range(len(first_with_0)):
    #         if first_with_0[i] != -1:
    #             while first_with_0[max_location] != first_with_0[i]:
    #                 if i == 0:
    #                     first_with_0[i] += bus_numbers[0]
    #                 else:
    #                     first_with_0[i] += bus_numbers[0] * bus_numbers[i]

    #                 if first_with_0[i] >= first_with_0[max_location]:
    #                     max_location = i

    #     for i in range(len(first_with_0)):
    #         if first_with_0[i] != -1:
    #             if first_with_0[i] != first_with_0[max_location]:
    #                 found = False
    #                 break
    #             found = True
    # flag = first_with_0[0]
    # print(flag)
part1()
part2()
