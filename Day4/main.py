import utilities


def part1():
    infile = open('Day4/input.txt', 'r', encoding=" ISO-8859-15")
    contents = infile.readlines()
    infile.close()

    passports = []
    start = 0
    for end in range(0, len(contents)):
        # print(contents[end])
        if contents[end] == '\n':
            passports.append(contents[start:end])
            start = end

    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for i in range(len(passports)):
        passports[i] = ''.join(passports[i])
        passports[i] = passports[i].replace('\n', ' ')
        passport = passports[i].split(' ')
        fields = []
        for value in passport:
            if value != '':
                field, _ = value.split(':')
                fields.append(field)

        reqCount = 0
        for req in requiredFields:
            if req in fields:
                reqCount += 1

        if reqCount == len(requiredFields):
            valid += 1

    print(valid)


infile = open('Day4/input.txt', 'r', encoding=" ISO-8859-15")
contents = infile.readlines()
infile.close()

passports = []
start = 0
for end in range(0, len(contents)):
    # print(contents[end])
    if contents[end] == '\n':
        passports.append(contents[start:end])
        start = end

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
for i in range(len(passports)):
    passports[i] = ''.join(passports[i])
    passports[i] = passports[i].replace('\n', ' ')
    passport = passports[i].split(' ')
    fields = []
    data = []
    for value in passport:
        if value != '':
            field, d = value.split(':')
            fields.append(field)
            data.append(d)

    reqCount = 0
    for j in range(len(fields)):
        if fields[j] == 'byr':
            if int(data[j]) >= 1920 and int(data[j]) <= 2002:
                reqCount += 1

        elif fields[j] == 'iyr':
            if int(data[j]) >= 2010 and int(data[j]) <= 2020:
                reqCount += 1

        elif fields[j] == 'eyr':
            if int(data[j]) >= 2020 and int(data[j]) <= 2030:
                reqCount += 1

        elif fields[j] == 'hgt':
            if data[j][-2:] == 'cm':
                if int(data[j][:-2]) >= 150 and int(data[j][:-2]) <= 193:
                    reqCount += 1

            elif data[j][-2:] == 'in':
                if int(data[j][:-2]) >= 59 and int(data[j][:-2]) <= 76:
                    reqCount += 1

        elif fields[j] == 'hcl':
            if data[j][0] == '#':
                for char in data[j][1:]:
                    if not char in '0123456789abcdef':
                        reqCount -= 1
                        break

                reqCount += 1

        elif fields[j] == 'ecl':
            if data[j] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                reqCount += 1

        elif fields[j] == 'pid':
            if len(data[j]) == 9:
                for char in data[j]:
                    if not char in '0123456789':
                        reqCount -= 1
                        break

                reqCount += 1
    if reqCount == len(requiredFields):
        valid += 1

print(valid)
