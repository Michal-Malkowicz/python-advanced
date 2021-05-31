def read_input(filename) -> list:
    file = open(filename, 'r').read()
    lines = file.split('\n')

    numbers = []
    for line in lines:
        numbers.append(int(line))
    return numbers


def get_result(numbers) -> int:
    result = 0
    for value1 in numbers:
        for value2 in numbers[1:]:
            if value1 + value2 == 2020:
                result = value1 * value2
                return result
        del numbers[0]


print(get_result(read_input('input.txt')))
