import random


def generateX(randomNum):
    x = randomNum.random()

    if x < 0.4:
        return 1
    elif x < 0.45:
        return 2
    elif x < 0.65:
        return 3
    else:
        return 4


def pickY(x, randomNum):
    if x == 1:
        y = randomNum.random()
        if y < 0.75:
            return 1
        return 4
    if x == 2:
        return 2
    if x == 3:
        return 4
    if x == 4:
        y = randomNum.random()
        if y < 0.8571:
            return 2
        return 4
    return 3


def main():

    randomNum = random.Random()
    stats = [[0] * 4 for _ in range(4)]
    for _ in range(100000):
        x = generateX(randomNum)
        y = pickY(x, randomNum)
        stats[x - 1][y - 1] += 1
    print("     ", end="")
    print()
    for x in range(len(stats)):
        print(x + 1, end=" ")
        print(stats[x])


if __name__  == '__main__':
    main()