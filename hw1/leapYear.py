def isLeapYear(yearForValidation):
    if (yearForValidation % 4) != 0:
        print("not leap")
        return False
    elif (yearForValidation % 100) == 0:
        if (yearForValidation % 400) == 0:
            print("leap")
            return True
        else:
            print("not leap")
            return False
    else:
        print("leap")
        return True


print("set year")
year = int(input())
isLeapYear(year)
