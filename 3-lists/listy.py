
# zagnieżdzenia funkcji w funkcji - pomnożenie funkcji razy 10
#power_values = [[a**2 for a in range(10) if not a % 2] for b in range(10)]
#print(power_values)

# tworzenie dwuelementowych lis klucz wartosc ( jak slownik )
#a = [[key, value for key, value in pssport.items()] for passport in passports]

#
with open('input.txt', 'r') as file:
    lines = file.readlines()

seat_rows = [line.strip() for line in lines]
print(seat_rows)
