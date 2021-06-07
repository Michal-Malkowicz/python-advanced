#
## acc - increases accu
## jmp - changing operation
## nop - skipp
#
## count accu - exit when index of instruction will be repeated
#
#accu, instructions, index, saved_indexes = 0, {}, 0, []
#
#with open('input.txt', 'r') as file:
#    lines = [line.split() for line in file.readlines() if line]
#
#print(lines)
#
#
#while index not in saved_indexes:
#    for i, line in enumerate(lines):
#        if i == index:
#            saved_indexes.append(index)
#            if line[0] == 'acc':
#                accu += int(line[1])
#                index += 1
#            elif line[0] == 'jmp':
#                index += int(line[1])
#            else:
#                index += 1
#            break
#print(accu)
#

# ta biblioteka mierzy czas wykonywania operacji:
#
#import timeit
#
#
#setup = '''
#input = [i for i in range(100000)]
#'''
#
#code = '''
#def power(input):
#    return input**2
#
#for i in input:
#    power(i)
#'''
#
#
#print(timeit.repeat(code, setup=setup))

# przyklad 2:


#mport timeit


#etup = '''
# input = [i for i in range(1000)]
#''

#ode1 = '''
#ist = [i for i in range(1000) if i%2]
#''

#ode2 = '''
#ist = []

#or i in range(10000):
#   if i%2:
#       list.append(i)
#''

#terations = 100000

#ime1 = timeit.timeit(code1, setup=setup, number=iterations)

#ime2 = timeit.timeit(code2, setup=setup, number=iterations)

#rint(f'Difference: {(time2-time1)/time2*100} %')

## przyklad 3
#
#import timeit
#
#
#setup = '''
#input = [i for i in range(1000)]
#'''
#
#code1 = '''
#5 in input
#'''
#
#code2 = '''
#for i in input:
#    if i==5:
#        break
#'''
#
#iterations = 100000
#
#time1 = timeit.timeit(code1, setup=setup, number=iterations)
#
#time2 = timeit.timeit(code2, setup=setup, number=iterations)
#
#print(f'Difference: {(time2-time1)/time2*100} %')

## przyklad 4
#
#import timeit
#
#
#setup = '''
#input = [i for i in range(1000)]
#'''
#
#code1 = '''
#input.sort()
#'''
#
#code2 = '''
#sorted(input)
#'''
#
#iterations = 100000
#
#time1 = timeit.timeit(code1, setup=setup, number=iterations)
#
#time2 = timeit.timeit(code2, setup=setup, number=iterations)
#
#print(f'Difference: {(time2-time1)/time2*100} %')

## przyklad 5
#
#import timeit
#
#
#setup = '''
##input = [i for i in range(1000)]
#'''
#
#code1 = '''
#lambda_function = lambda a, b: a ** b
#a = lambda_function(1, 2)
#'''
#
#code2 = '''
#def def_fuction(a, b):
#    return a**b
#a = def_fuction(1,2)
#'''
#
#iterations = 100000
#
##lambda_function = lambda a, b: a * b
##
##print(lambda_function(1, 2))
#
#time1 = timeit.timeit(code1, number=iterations)
#
#time2 = timeit.timeit(code2, number=iterations)
#
#print(f'Difference: {(time2-time1)/time2*100} %')

# przyklad 6

import timeit


setup = '''
input = [i for i in range(100000)]
'''

code1 = '''
input.pop(0)
'''

code2 = '''
del input[0]
'''

iterations = 100000

for i in range(10):
    time1 = timeit.timeit(code1, setup=setup, number=iterations)
    time2 = timeit.timeit(code2, setup=setup, number=iterations)
    print(f'Difference: {(time2-time1)/time2*100} %')

