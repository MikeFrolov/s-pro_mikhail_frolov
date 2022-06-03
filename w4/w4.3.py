def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fib_list(n):
    # return [i for i in fib_generator(n)]
    a, b = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
