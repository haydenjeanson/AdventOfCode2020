import utilities

lines = utilities.get_lines('Day7/input.txt')


class Bag():
    def __init__(self, colour, children):
        self.colour = colour
        self.children = children


def getBagOfColour(colour):
    for bag in allBags:
        if bag.colour == colour:
            return bag


def parseLine(line):
    l, r = line.split(' contain ')
    colour = l[:-5]

    r = r[:-1]
    childrenList = r.split(', ')
    childrenDict = {}
    for child in childrenList:
        if child[-1] == 's':
            childrenDict[child[2:-5]] = child[0]
        else:
            childrenDict[child[2:-4]] = child[0]

    newBag = Bag(colour, childrenDict)

    return newBag


def part1():
    def bag_recursion(currentBag):
        # base cases: shiny gold or no further bags

        if currentBag is None:
            return 0
        elif currentBag.colour == 'shiny gold':
            return 1
        else:
            for child in currentBag.children:
                if child == ' other':
                    continue
                if bag_recursion(getBagOfColour(child)) == 1:
                    return 1
            return 0

    goldCount = 0
    for bag in allBags:
        if bag.colour != 'shiny gold':
            goldCount += bag_recursion(bag)

    print(goldCount)


def part2():
    def bag_recursion(currentBag):
        # base cases: shiny gold or no further bags

        if currentBag is None:
            return 0
        else:
            bagSum = 0
            for child in currentBag.children:
                try:
                    multiplier = int(currentBag.children[child])
                except ValueError:
                    continue
                sumOfChild = bag_recursion(getBagOfColour(child))
                bagSum += multiplier + (multiplier * sumOfChild)
            return bagSum

    allBags = []
    for line in lines:
        allBags.append(parseLine(line))

    shinyGoldBag = getBagOfColour('shiny gold')
    print(bag_recursion(shinyGoldBag))


allBags = []
for line in lines:
    allBags.append(parseLine(line))

part1()
part2()
