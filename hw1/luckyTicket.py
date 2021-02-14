def twoTicketsInRow():
    counter = 0
    for runner in range(100000, 999999):
        digits = [int(d) for d in str(runner)]
        digSum = 0
        # print(digits)
        for digitsRunner in digits:
            digSum += int(digitsRunner)
        if digSum % 7 == 0:
            counter = counter + 1
        else:
            counter = 0
        if counter == 2:
            print(runner, " ", runner - 1)
            return True
    return False
#
print(twoTicketsInRow())