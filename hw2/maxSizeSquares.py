
def maxSquareSize(length, width, amount = 0):
    if (length <= 0) | (width <= 0):
        raise RuntimeError("length or width must be positive")
    elif length == 1 == width:
        print("total squares amount is " + str(amount))
        return 1
    elif length == width:
        print("length is equal to width (side = " + str(width) + ")")
        print("total squares amount is " + str(amount))
        return width
    elif length > width:
        print("your square side is " + str(width))
        return maxSquareSize(length - width, width, amount + 1)
    elif length < width:
        print("your square side is " + str(length))
        return maxSquareSize(length, width - length, amount + 1)


length = int(input("set rectangle length:\n"))
width = int(input("set rectangle width:\n"))

print(maxSquareSize(length, width))
