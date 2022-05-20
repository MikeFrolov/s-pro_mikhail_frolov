""" Определения positive() и negative() могут как предшествовать, так и следовать определению test(),
это никак не повлияет на выполнение программы, так как их вызов происходит внутри ф-ции test(), которая
вызывается уже после их определения. В таком случае, positive() и negative() попадают в область видимости."""


def test():
    while True:
        get_str = input("Enter an integer: ")
        try:
            return positive() if int(get_str) >= 0 else negative()
        except ValueError:
            print("Error: Invalid value entered!")


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


if __name__ == "__main__":
    test()
