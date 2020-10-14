#Zgadnij jaka to liczba - gra
import random

print('Witaj. Jak masz na imię?')
imie = input()

print(f'Okej {imie}, myślę o liczbie z zakresu 1 do 20')
liczba = random.randint(1,20)


for iloscProb in range(1, 7):
    print('Zgadnij jaka to liczba')
    odpowiedz = int(input())

    if odpowiedz < liczba:
        print('Twoja odpowiedź jest za niska')
    elif odpowiedz > liczba:
        print('Twoja odpowiedź jest za wysoka')
    else:
        break #Prawidłowa odpowiedź
    
if odpowiedz == liczba:
    print(f'Brawo {imie}, zgadłeś moją liczbę w {iloscProb} próbach.')
else:
    print(f'Niestey, moja liczba to {liczba}.')
