import string


def punctuation_cleaning(line: str) -> str:
    return line.translate(str.maketrans('', '', string.punctuation))


def word_list(line: str) -> list:
    clear_line = punctuation_cleaning(line)  # used punctuation_cleaning function
    return [word for word in clear_line.split(" ") if word != '']