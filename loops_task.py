import time

# while
licznik = 0
czas1 = time.time()
while True:
    licznik += 1
    if licznik >= 20:
        break

czas_while = time.time() - czas1

# for
czas1 = time.time()
for x in range(20):
    pass

czas_for = time.time() - czas1


print(f'Czas while = {czas_while}, Czas for = {czas_for}')
