import random


def deleteValues(array):
    runner = 1
    while runner < len(array):
        if runner % 2 == 0:
            del array[runner]
        runner = runner + 1


def fillTheArray(arrayLength):
    result = []
    runner = 0
    while runner < arrayLength:
        result.append(random.randint(0, 99))
        runner = runner + 1
    return result


print("set array length")
length = int(input())
array = fillTheArray(length)
print(array)
deleteValues(array)
print(array)
