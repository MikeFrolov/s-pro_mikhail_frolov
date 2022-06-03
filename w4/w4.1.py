class FormulaError(Exception):
    def __init__(self, message="FormulaError"):
        self.message = message
        super().__init__(self.message)


def calc(expression: str):
    values = [i for i in expression.split(" ")]

    if len(values) != 3:
        raise FormulaError("The input string must have 3 elements separated by a space!")
    try:
        a, b = float(values[0]), float(values[2])
    except ValueError:
        raise FormulaError("The first and third elements of the string must be an integer or a float")

    try:
        operators = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}
    except ZeroDivisionError:
        raise FormulaError("ERROR: Division by zero!")

    if values[1] not in operators:
        raise FormulaError("The second element of string must be: '+' or '-' or '*' or '/'")

    return operators[values[1]]
