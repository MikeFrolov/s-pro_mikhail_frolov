from functools import reduce


def str_concat():
    return input("Enter the first string: ") + input("Enter the second string: ")


def multi():
    l = [1]
    while True:
        try:
            num = float(input("Enter the number: "))
            if num != 0:
                l.append(num)
            else:
                break
        except ValueError:
            print("Error: Invalid value entered!")

    if len(l) > 1:
        multiple = round(reduce(lambda a, b: a * b, l), 2)
        return int(multiple) if multiple.is_integer() else multiple

    return 0


if __name__ == "__main__":
    print('Concatenated strings:', str_concat())
    print('Multiplication result =', multi())
