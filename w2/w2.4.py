def getInput() -> str:
    return input("Enter the string or int: ")


def testInput(entered_string: str) -> bool:
    if entered_string.isdigit() or entered_string[1:len(entered_string)].isdigit():
        return True
    return False


def strToInt(entered_string: str) -> int:
    return int(entered_string)


def printInt(num: int) -> None:
    print(num)


if __name__ == "__main__":
    string = getInput()

    if testInput(string):
        printInt(strToInt(string))
