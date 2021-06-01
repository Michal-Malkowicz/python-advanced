import re


# a = [1, 2, 3]
# a = [str(element) for element in a]
#
# text = "test".join(a)
##
## print(text.replace("test", " "))
#
#
# with open('input.txt', 'r') as my_file:
#    lines = my_file.readlines()
#
#passports, passport, records = [], {}, []
#
# for line in lines:
#
#    if line.strip():
#        records.extend(line.split())
#    else:
#        for record in records:
#            passport[key] = value
#        passport.append(passport)
#        passport, records = {}, []
#
# print(passports)


def agregate_people(filename: str) -> list:
    file = open(filename, 'r').read()
    persons = file.split('\n\n')

    passports = []
    for person in persons:
        person = person.replace('\n', ' ')
        person_datas = person.strip().split(' ')

        temp_dict = {}
        for data in person_datas:
            content = data.split(':')
            temp_dict[content[0]] = content[1]
        passports.append(temp_dict)

    return passports


# print(agregate_people('input.txt'))


def validate(passports: list) -> list:
    mandatory, result, index = ['byr', 'iyr',
                                'eyr', 'hgt', 'hcl', 'ecl', 'pid'], [], 0

    for passport in passports:
        for id in mandatory:
            if id not in passport.keys():
                result.append(index)
                break
        index += 1
    return result


# passports = agregate_people('input.txt')
# wrong_ids = validate(passports)
# print(f'Passports:\n {len(passports)}\nWrong ids:\n {len(wrong_ids)}\nList of wrong ids:\n{wrong_ids}')


def compare(temp_contener: dict, key: str, value: str, length: int, lower_value: int, upper_value: int) -> dict:
    if (len(value) == length) and (lower_value <= int(value, 10) <= upper_value):
        temp_contener['result'].append(f'{key} valid: {value}')
    else:
        temp_contener['result'].append(f'{key} invalid: {value}')
        temp_contener['counter'] += 1
    return temp_contener


#def  hcl(color):
#
#    return bool(re.search(r'[#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', color))
#
#def  ecl(color):
#
#    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#    return bool(color  in  valid_colors)
#
#def  pid(input_number):
#
#    return bool(re.search(r'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', input_number))
#cid
#jest
#nieważne
#

def regex_finder(temp_contener: dict, key: str, value: str) -> dict:
    if key == 'hgt':
        str_to_compare = re.findall(r'^\d{1,3}[a-zA-Z]{2}$', value)
    elif key == 'hcl':
        str_to_compare = re.findall(r'^#[0-9a-f]{6}$', value)
    elif key == 'ecl':
        str_to_compare = re.findall(r'^blu|amb|brn|grn|gry|hzl|oth$', value)
    elif key == 'pid':
        str_to_compare = re.findall(r'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', value)
    else:
        str_to_compare = [' ']

    if not str_to_compare:
        temp_contener['result'].append(f'{key} invalid: {value}')
        temp_contener['counter'] += 1
    elif value == str_to_compare[0]:
        temp_contener['result'].append(f'{key} valid: {value}')
    else:
        temp_contener['result'].append(f'{key} valid: {value}')

    return temp_contener


def check_correctness(passports: list) -> dict:
    temp_content = {'result': [], 'counter': 0, 'failed_passport': 0}

    for passport in passports:
        for key, value in passport.items():
            if key == 'byr':
                temp_content = compare(temp_content, key, value, 4, 1920, 2002)
            elif key == 'iyr':
                temp_content = compare(temp_content, key, value, 4, 2010, 2020)
            elif key == 'eyr':
                temp_content = compare(temp_content, key, value, 4, 2020, 2030)
            else:
                temp_content = regex_finder(temp_content, key, value)

        if temp_content['counter'] != 0:
            temp_content['failed_passport'] += 1
            temp_content['counter'] = 0

    return temp_content


temp_contener = check_correctness(agregate_people('input.txt'))
for index in temp_contener['result']:
    print(index)
print(temp_contener['failed_passport'])

# print(locals()[key](value) -> # calling function by name

#test_string = '888 409404'
#result = re.findall('\d{3} ?\d{3} ?\d{3} ?', test_string)
# print(result)
#
# printowanie tylko jak jest wyniki:
# if result:
#    print(result)
