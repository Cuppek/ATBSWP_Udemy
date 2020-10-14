# Program mówi cześć i pyta o imię

print('Witaj świecie!')

print('Jak masz na imię?') #Pytanie o imię
mojeImie = input()
print('Miło Cię poznać, ' + mojeImie)
print('Długość Twojego imienia to: ')
print(len(mojeImie))

print('Ile masz lat?') #Pytanie o wiek
wiek = input()
print('W ciągu roku będziesz miał ' + str(int(wiek) + 1))
