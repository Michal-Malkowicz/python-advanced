# a = [1, 2, 3]
# a = [str(element) for element in a]
#
# text = "test".join(a)
##
## print(text.replace("test", " "))
#
#
#with open('input.txt', 'r') as my_file:
#    lines = my_file.readlines()
#
#passports, passport, records = [], {}, []
#
#for line in lines:
#
#    if line.strip():
#        records.extend(line.split())
#    else:
#        for record in records:
#            passport[key] = value
#        passport.append(passport)
#        passport, records = {}, []
#
#print(passports)


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


#print(agregate_people('input.txt'))


def validate(passports: list) -> list:
    mandatory, result, index = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], [], 0

    for passport in passports:
        for id in mandatory:
            if id not in passport.keys():
                result.append(index)
                break
        index += 1
    return result


passports = agregate_people('input.txt')
wrong_ids = validate(passports)
print(f'Passports:\n {len(passports)}\nWrong ids:\n {len(wrong_ids)}\nList of wrong ids:\n{wrong_ids}')




