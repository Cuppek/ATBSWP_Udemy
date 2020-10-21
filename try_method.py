spam = [1,2,3,4,5,6]
liczba = int(input('Wpisz liczbę '))
try:
    print(spam.index(liczba))
except ValueError:
    print('Liczba spoza zakresu')
