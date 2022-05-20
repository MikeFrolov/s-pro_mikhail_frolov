from random import randint


# Function for the second task
def flipped_dict(dictionary: dict) -> dict:
    flip_dict = {v: k for k, v in dictionary.items()}
    return flip_dict


if __name__ == "__main__":

    # First task
    school = {f'{i}{k}': randint(1, 20) for i in range(1, 12) for k in 'abc'}
    school['1a'] = 25
    school['1d'] = 22
    del school['1c']
    print('Sum of students:', sum(school.values()))

    # Second task
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    flipped_dict(my_dict)

    print('My dict:', my_dict)
    print('My flipped dict:', flipped_dict(my_dict))
