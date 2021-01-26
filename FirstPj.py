import random

myList = [12, 34, 45, 3, -1, 425, 4, 12, 34]

print("=============================")

for runner in range(1, 8):
    if (myList[runner] > myList[runner - 1]) and (myList[runner] > myList[runner + 1]):
        print(runner)
