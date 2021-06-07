
# zagnieżdzenia funkcji w funkcji - pomnożenie funkcji razy 10
#power_values = [[a**2 for a in range(10) if not a % 2] for b in range(10)]
#print(power_values)

# tworzenie dwuelementowych lis klucz wartosc ( jak slownik )
#a = [[key, value for key, value in pssport.items()] for passport in passports]

#

#max_row, min_row, max_collumn, min_collumn = 127, 0, 7, 0
#
#for seat in seat_rows:
#    temp = []
#    temp.extend(seat)
#    for a in temp:
#        if a == 'F':
#        if a == 'B':
#
#    pointer = [128/2 for a in
#
with open('input.txt', 'r') as file:
    lines = file.readlines()

seats = [line.strip() for line in lines]


def count_seats(seats):
    seats_ids = []
    for seat in seats:

        row = seat[:7].replace('B', '1').replace('F', '0')
        row_int = int(row, 2)
        column = seat[-3:].replace('R', '1').replace('L', '0')
        column_int = int(column, 2)
        seat_id = row_int * 8 + column_int
        seats_ids.append(seat_id)

    return seats_ids


# print(max(count_seats(seats)))


def find_seat(seats):
    seats.sort()
    for i in range(len(seats)):
        if seats[i + 1] != seats[i] + 1:
            break
    return seats[i + 1]


print(find_seat(count_seats(seats)))



