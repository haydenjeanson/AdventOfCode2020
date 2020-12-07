import utilities


def part1():
    inputText = utilities.file_to_text('Day6/input.txt')

    groups = inputText.split('\n\n')

    totalSum = 0
    for group in groups:
        customsDict = {chr(ord('a') + i): 0 for i in range(26)}

        for char in group:
            if char in customsDict:
                customsDict[char] = 1

        totalSum += sum(customsDict.values())

    print(totalSum)


part1()


def part2():
    inputText = utilities.file_to_text('Day6/input.txt')

    groups = inputText.split('\n\n')

    totalSum = 0
    for group in groups:
        customsDict = {chr(ord('a') + i): 0 for i in range(26)}
        lines = group.split('\n')
        for line in lines:
            for char in line:
                if char in customsDict:
                    customsDict[char] += 1

        for key in customsDict:
            if type(lines) == list:
                if customsDict[key] == len(lines):
                    totalSum += 1
            else:
                if customsDict[key] == 1:
                    totalSum += 1

    print(totalSum)


part2()
