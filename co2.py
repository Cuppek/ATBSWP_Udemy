start = int(input('Wpisz liczbę początkową: '))
koniec = int(input('Wpisz liczbę końcową: '))

if (start % 2) == 1:
    start += 1

koniec += 1
    
print(str(start) + ' ' + str(koniec))
print(list(range(start, koniec, 2)))
