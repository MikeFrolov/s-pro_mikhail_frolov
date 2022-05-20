def num_to_unicode():
    while True:
        try:
            n = int(input("Enter character number of the Unicode table: "))
            if n == 0:
                break
            print(chr(n))
        except UnicodeEncodeError:
            """This exception helps to avoid the error of converting surrogate number to 'utf-8' symbol.
            The range of such numbers: 55296 - 57343"""

            print("This character is surrogate and cannot be encoded in 'utf-8' symbol!")
        except (ValueError, OverflowError):
            """This exception helps to avoid errors when entering an integer value that is too long
            and a value that cannot be converted to integer"""

            print("Error: The value must be integer between 0 and 1114111")


def len_str():
    while True:
        input_str = input("Please enter a message no longer than 10 characters: ")
        if len(input_str) > 10:
            print("Error: Too long message entered!")

        else:
            print(input_str + "*" * (10 - len(input_str)))
            break


def min_max_floats():
    while True:
        get_nums = input("Enter 6 floating-point numbers or integers separated by commas: ")
        list_items = [_ for _ in get_nums.split(',')]
        if len(list_items) < 6:
            print("Error: Few values entered!")
        elif len(list_items) > 6:
            print("Error: Extra values entered!")
        else:
            try:
                list_nums = [float(i) for i in list_items]
                print(f"Result: {sorted(list_nums)[0]}, {sorted(list_nums)[-1]}")
                break
            except ValueError:
                print('Error: One or more of the entered values is not a number!')


if __name__ == "__main__":
    num_to_unicode()
    len_str()
    min_max_floats()
