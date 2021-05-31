def read_input(filename: str) -> list:
    """

    :param filename:
    :return: list
    """

    file = open(filename, 'r').read()
    lines = file.split('\n')

    numbers = []
    for line in lines:
        numbers.append(int(line))
    return numbers


def get_result(numbers: list) -> int:
    """
    Open file and return a stream.  Raise OSError upon failure.

    :param numbers: lista
    :return: int
    """

    for value1 in numbers:
        for value2 in numbers[1:]:
            if value1 + value2 == 2020:
                return value1 * value2
        numbers.pop(0)


print(get_result(read_input('input.txt')))
