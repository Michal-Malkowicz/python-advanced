import re


def read_file():
    file = open('input.txt', 'r').read()
    lines = file.split('mask ')

    masks = {}
    for line in lines:
        if line != '':

            lines2 = line.split('\n')
            content = {}
            for line2 in lines2:
                if line2 == '':
                    pass
                elif line2[:2] == '= ':
                    mask = line2[3:38]
                else:
                    mem = re.findall(r'\[(\d*)\]', line2)[0]
                    value = re.findall(r'= (\d*)', line2)[0]
                    content[mem] = value
            masks[mask] = content

    return masks


print(read_file())

