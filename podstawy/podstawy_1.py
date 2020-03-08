# --------------------------------------------------------------------
# Napisz program, który wyświetli napis „Hello world”.

print("Początek programowania")
print("Hello World!")
# --------------------------------------------------------------------
# Napisz program, w którym utworzysz trzy zmienne o dowolnych nazwach,
# którym przypiszesz następujące wartości: 10, „b”, 3.7
# Następnie wypisz ich wartości oraz typy.

a = 10
b = "b"
c = 3.7
print("a, b ,c")
# --------------------------------------------------------------------
# Utwórz nową zmienną i przypisz do niej wynik dodawania zmiennej
# pierwszej i trzeciej, wypisz jej wartość na ekran.

d = a + c
print("Nowa zmienna to", d)
# --------------------------------------------------------------------
# Zwiększ nowoutworzoną zmienną o 10, wypisz jej wartość.

e = d + 10
print("Powiekszona zmienna to", d)
# --------------------------------------------------------------------
# Utwórz zmienną i przypisz jej swoje imię, a następnie wyświetl na ekran.

myName = "Michał"
print(myName)
# --------------------------------------------------------------------
# Napisz program, który pobierze od użytkownika wysokość i długość
# podstawy trójkąta, a następnie obliczy i wypisze na ekran jego pole
# powierzchni.

wys = int(input("Podaj wysokość trójkąta: \n"))
dl = int(input("Podaj długość trójkąta: \n"))
pole = 0.5 * wys * dl
print("Pole trójkąta to", pole)
# --------------------------------------------------------------------
# Napisz program, który obliczy pole powierzchni koła dla wybranej przez
# użytkownika długości promienia.

r = float(input("Podaj promień koła: \n"))
pi = 3.14
pole = pi * r ** 2
print("Pole koła", pole)
# --------------------------------------------------------------------
# Napisz program, który zapyta użytkownika o imię i nazwisko. Następnie,
# korzystając ze specyfiki zmiennych tekstowych, wypiszesz na ekran
# jego/jej inicjały.

yourName = input("Jak masz na imię? ")
yourLastName = input("Jak masz na nazwisko? ")
print(yourName[0].capitalize(),yourLastName[0].capitalize(), sep="")
# --------------------------------------------------------------------
# Napisz program, który zapyta użytkownika o imię, nazwisko oraz wiek.
# Następnie wyświetli pobrane wartości w jednej linii oddzielone spacjami.

yourName2 = input("Jak masz na imię? ")
yourLastName2 = input("Jak masz na nazwisko? ")
yourAge = input("Ile masz lat? ")
print(yourName2, yourLastName2, yourAge)
# --------------------------------------------------------------------
# Zapisz dane o pracowniku (imię, nazwisko, wiek, pensja, stanowisko) w
# osobnych zmiennych. Następnie tak sformatuj wyjście z programu aby
# poprawnie wypisywał informacje o pracowniku, np.: Pan Adam Kowalski
# (wiek: 35 lat) pracuje na stanowisku: młodszy inżynier procesu
# (pensja: 6000 brutto).

yourName3 = input("Jak masz na imię? ")
yourLastName3 = input("Jak masz na nazwisko? ")
yourAge2 = input("Ile masz lat? ")
yourSalary = input("Ile wynośi Twoja miesięczna wypłata? ")
yourJobPosition = input("Na jakim stanowisku jesteś w pracy? ")

print(f"Pan/Pani {yourName3} (wiek: {yourAge2}) pracuje na stanowisku: {yourJobPosition} (pensja: {yourSalary})")
# --------------------------------------------------------------------
# Dodaj do siebie liczby 10 i 20. Następnie wynik podziel przez 2. Od
# otrzymanego wyniku odejmij 5. Następnie pomnóż wynik przez 3.
# Wykonaj wszystko w jednej instrukcji.

print((((10+20)/2)-5)*3)
# --------------------------------------------------------------------
# Napisz program, który wypisze na ekran trzykrotnie wartość dowolnej
# zmiennej tekstowej.

threeTimes = "Python jest super."
print((threeTimes + " ") * 3)
# --------------------------------------------------------------------
# Napisz program, który wyświetli napis „Hello world” w dwóch liniach.

print("Hello\nWorld")
# --------------------------------------------------------------------
# Napisz program, który pobierze od użytkownika dowolny napis, a
# następnie wypisze go na ekranie w takiej formie, że wszystkie litery
# zostaną zamienione na wielkie.

randomText = input("Podaj jakieś słowo: ")
print(randomText.upper())
# --------------------------------------------------------------------
# Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli
# informację czy jest parzysta, czy też nie.

randomDigit = int(input("Podaj dowolną liczbę całkowitą: "))
if randomDigit % 2 == 0:
    print(f"Twoja liczba {randomDigit} jest parzysta.")
else:
    print(f"Twoja liczba {randomDigit} jest nieparzysta.")
# --------------------------------------------------------------------
# Napisz program, który sprawdzi, czy podana przez użytkownika wartość
# mieści się w przedziale od 0 do 9 (włącznie).

randomDigit2 = int(input("Podaj dowolną liczbę całkowitą: "))
if 0 <= randomDigit2 <= 9:
    print(f"Twoja liczba {randomDigit2} mieści się w przedziale.")
else:
    print(f"Twoja liczba {randomDigit2} nie mieści się w przedziale.")
# --------------------------------------------------------------------
# Napisz program, który wystawi ocenę z testu.
# 0 - 20 pkt - ocena niedostateczna
# 21 - 40 pkt - ocena dopuszczająca
# 41 - 60 pkt - ocena dostateczna
# 61 - 80 pkt - ocena dobra
# Powyżej 80 pkt – ocena bardzo dobra

points = int(input("Podaj ilość punktów: "))
if 0 <= points <= 20:
    print(f"Punkty: {points}. Ocena niedostateczna.")
elif 20 < points <= 40:
    print(f"Punkty: {points}. Ocena dopuszczająca.")
elif 40 < points <= 60:
    print(f"Punkty: {points}. Ocena dopuszczająca.")
elif 60 < points <= 80:
    print(f"Punkty: {points}. Ocena dobra.")
elif points > 80:
    print(f"Punkty: {points}. Ocena bardzo dobra.")
else:
    print("Jeżeli widziesz ten komunikat skontaktuj sie z programistą")
# --------------------------------------------------------------------
# Napisz program, zapyta użytkownika o rok jego urodzenia, a następnie
# zwróci informację o tym, czy jest pełnoletni.

yourAge3 = int(input("Podaj swój rok urodzenia: "))
currentYear = 2019
work = currentYear - yourAge3
if work >= 18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnoletni")
# --------------------------------------------------------------------
# Napisz program, który zapyta użytkownika o nazwę miesiąca, a następnie
# zwróci informację, ile dany miesiąc ma dni.

months = {"styczeń": 31,
          "luty": "28 lub 29",
          "marzec": 31,
          "kwiecień": 30,
          "maj": 31,
          "czerwiec": 30,
          "lipiec": 31,
          "sierpień,": 31,
          "wrzesień": 30,
          "październik": 31,
          "listopad": 30,
          "grudzień": 31
            }
question = input("Podaj nazwe miesiąca, a powiem Ci ile ma dni: ").lower()
questionDict = (months.get(question))
if questionDict:
    print(f"{question.capitalize()} ma", questionDict, "dni.")
else:
    print("Nazwa miesiąca nieprawidłowa.")
# --------------------------------------------------------------------
# Napisz program, który zwróci wartość bezwzględną danej liczby.

yourDigit = float(input("Podaj dowolną liczbę: "))
if yourDigit < 0:
    print(yourDigit * (-1))
else:
    print(yourDigit)
# --------------------------------------------------------------------
# Napisz program, który pobierze od użytkownika dwie liczby i wypisze
# większą z nich.

digit1 = float(input("Podaj liczbę: "))
digit2 = float(input("Znów podaj liczbę: "))
if digit1 > digit2:
    print("Większą liczbą jest: ", digit1)
elif digit1 < digit2:
    print("Większą liczbą jest: ", digit2)
elif digit1 == digit2:
    print("Obydwie liczby są sobie równe.")
else:
    print("Jeżeli widziesz ten komunikat skontaktuj sie z programistą")
# --------------------------------------------------------------------
# Napisz program, który w przyjaznej dla użytkownika formie zwróci
# informację o jego stanie na podstawie BMI.

wzrost = float(input("Podaj swój wzrost w metrach: "))
waga = float(input("Podaj swoją wagę w kg: "))
bmi = waga / wzrost ** 2
if bmi < 18.50:
    print(f"Twoje BMI wynosi {bmi}, a oznacza to niedowagę.")
elif bmi < 25:
    print(f"Twoje BMI wynosi {bmi}, a oznacza to optimum.")
elif bmi < 30:
    print(f"Twoje BMI wynosi {bmi}, a oznacza to nadwagę.")
else:
    print(f"Twoje BMI wynosi {bmi}, a oznacza to otyłość.")
# --------------------------------------------------------------------
# Utwórz listę zawierającą siedem artykułów spożywczych. Wyświetl na
# ekranie pierwszy i trzy ostatnie elementy listy.

lst = ["mleko", "sok", "dżem", "chleb", "masło", "dżem", "czekolada"]
print(lst[0])
print(lst[-3:])
# --------------------------------------------------------------------
# Utwórz listę pięciu liczb naturalnych. Następnie dodaj dwie nowe na jej
# koniec. Usuń trzeci element.

lst2 = [45, 78, 44, 98, 32]
lst2.extend([14, 55])
print(lst2)
del lst2[2]
print(lst2)
# --------------------------------------------------------------------
# Wypisz na ekran posortowaną listę z poprzedniego zadania.

print(sorted(lst2))

lst2.sort()
print(lst2)
# --------------------------------------------------------------------
# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr
# na formę tekstową, np.: 112 - > „jeden jeden dwa”

keys = {1:"jeden",
        2:"dwa",
        3:"trzy",
        4:"cztery",
        5:"pięć",
        6:"sześć",
        7:"siedem",
        8:"osiem",
        9:"dziewięć",
        0:"zero"}
yourNumber = int(input("Podaj liczbę: "))
lst3 = [int(x) for x in list(str(yourNumber))] # zamiania na listę
toKeys = []
for liczba in range(0,len(lst3)):
    toKeys.append(keys.get(lst3[liczba]))
print(" ".join(toKeys))
# --------------------------------------------------------------------
# Wyświetl kwadraty liczb od 3 do 9.

lst4 = []
for digit in range(3,10):
    lst4.append(digit ** 2)
print(lst4)
# --------------------------------------------------------------------
# Stwórz listę zawierającą parzyste liczby naturalne mniejsze od 99.

lst5 = []
digit3 = 0
while digit3 < 100:
    if digit3 % 2 == 0:
        lst5.append(digit3)
    digit3 += 1
print(lst5)
# --------------------------------------------------------------------
# Stwórz listę zawierającą kilka liczb całkowitych, a następnie program,
# który policzy sumę jej elementów, iterując po nich.

lst6 = [50, 50, 50, 50, 50]
digit4 = 0
for digit in lst6:
    digit4 += digit
print(digit4)
# --------------------------------------------------------------------
# Zmodyfikuj program, aby policzyć średnią po wszystkich elementach
lst7 = [50, 50, 50, 50, 50]
digit4 = 0
for digit in lst7:
    digit4 += digit/len(lst6)
print(digit4)
# --------------------------------------------------------------------
# A teraz program, który policzy iloczyn jej elementów, iterując po nich.
lst8 = [50, 50, 50, 50, 50]
digit4 = 1
for digit in lst8:
    digit4 *= digit
print(digit4)
# --------------------------------------------------------------------
# Znajdź indeks elementu największego na liście.
lst8 = [50, 67, 13, 78, 157]
high = 0
inx = 0
for digit in range(0,len(lst8)):
    if lst8[digit] > high:
        high = lst8[digit]
        inx = digit + 1
print(f"Najwyższa liczba to: {high}, a jej kolejność to: {inx} z rzędu.")
# --------------------------------------------------------------------
# Napisz program sprawdzający, czy podane przez użytkownika hasło jest poprawne.
# Poprawne hasło definiuje się w tym przypadku w ten sposób: posiada przynajmniej
# jedną dużą literę, jedną cyfrę, jeden znak specjalny [@, $, #], jest minimalnej
# długości 6 znaków i maksymalnej 15

zmienna = input("Podaj swoje hasło: ")
tablica = ["@", "$", "#"]

# Czy jest cyfra
walidacja1 = 0
for i in range(0, len(zmienna)):
    if zmienna[i].isdigit() == True:
        walidacja1 += 1
if walidacja1 <= 0:
    walidacja1t = "\n• cyfry"
else:
    walidacja1t = ""

# Czy jest duża litera
walidacja2 = 0
for i in range(0, len(zmienna)):
    if zmienna[i].isupper() == True:
        walidacja2 += 1
if walidacja2 <= 0:
    walidacja2t = "\n• dużej litery"
else:
    walidacja2t = ""

# Czy jest znak specjalny z tablicy
walidacja3 = 0
for i in range(0, len(zmienna)):
    if (zmienna[i] in tablica):
        walidacja3 += 1
if walidacja3 <= 0:
    walidacja3t = "\n• znaku specjalnego"
else:
    walidacja3t = ""

# Czy jest odpowiednia liczba znaków
walidacja4 = 0
for i in range(0, len(zmienna)):
    if 6 <= len(zmienna) <= 15:
        walidacja4 = 1
if walidacja4 <= 0:
    walidacja4t = "\n• odpowiedniej ilości znaków (6-15)"
else:
    walidacja4t = ""

if walidacja1 > 0 and walidacja2 > 0 and walidacja3 > 0 and walidacja4 > 0:
    print("TWOJE HASŁO JEST SILNE!")
else:
    print("W TWOIM HAŚLE BRAKUJE:", walidacja1t, walidacja2t, walidacja3t, walidacja4t)
# --------------------------------------------------------------------
# Napisz program, który pobierze 5 słów od użytkownika, a następnie
# wypisze najdłuższe z nich.

question6 = []
while len(question6) < 5:
    question6.append(input("Podaj słowo: "))

high2 = 0
inx = 0
for i in range(0, len(question6)):
    if len(question6[i]) > high2:
        high2 = len(question6[i])
        inx = i

print("Najdłuższym słowem jest:", question6[inx], "\n\n")
# --------------------------------------------------------------------
# Napisz program, który obliczy liczbę małych i wielkich liter w ciągu.

question7 = input("Podaj jakieś zdanie: ")
question7 = question7.replace(" ","")

small = 0
big = 0

for i in range(0, len(question7)):
    if question7[i] == question7[i].upper():
        big += 1
    if question7[i] == question7[i].lower():
        small += 1
print(f"Małe literki: {small}\nDuże literki: {big}")
# --------------------------------------------------------------------
# Napisz program, w którym zdefiniujesz dwie listy, a następnie sprawdzisz,
# czy pierwsza zawiera się w drugiej.

lst4 = ["samochód", "drzewo", "klawiatura", "komoda", "1"]
lst5 = ["telewizor", "drzwi", "samochód", "komoda", "myszka", "samochód", "klawiatura", "drzewo"]

diff = set(lst4) & set(lst5)

if len(diff) == len(lst4):
    print("Cała lista zawiera się w drugiej liście.")
else:
    print(f"Tylko te elementy {diff} zawarte są w drugiej liście.")
# --------------------------------------------------------------------
# Pobierz od użytkownika wartość n, a następnie stwórz słownik, którego
# elementy dla i < n będą postaci: (i, i2)

n = int(input("Podaj liczbę: "))
mydict = {}
for i in range(0, n):
    mydict[i] = i ** 2
print(f"Twój słownik: {mydict}")
# --------------------------------------------------------------------
# Napisz program, który poprosi użytkownika o podanie słowa i napisze,
# czy jest ono izogramem (słowo, w którym żadna litera się nie powtórzyła,
# np. „skrzynia”)

word = input("Podaj słowo: ")
word_lst = list(word)
word_set = set(word_lst)

if len(word_lst) == len(word_set):
    print("Słowo jest izogramem")
else:
    print("Słowo nie jest izogramem")
# --------------------------------------------------------------------
# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# palindromem (tj. czytany od przodu i wspak jest dokładnie taki sam, np.
# „kajak”, „Madam”, „nurses run”).

def palindrom(word):
    if word[0] == word[-1]:
        print("Słowo jest palindromem")
    else:
        print("Słowo nie jest palindromem")


word = input("Podaj słowo: ").lower().replace(" ", "")

palindrom(word)
# --------------------------------------------------------------------
# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# pangramem (tj. zawiera każdą literę alfabetu co najmniej raz, np. „The
# quick brown fox jumps over the lazy dog”).

def pangram(n):
    import string
    alphabet = set(string.ascii_lowercase)
    if alphabet.issubset(n):
        return "Zdanie posiada wszystkie litery alfabetu"
    else:
        return "Zdanie nie posiada wszystkich literek alfabetu"


n = set("The quick brown fox jumps over the lazy dog".lower().replace(" ", ""))

print(pangram(n))
# --------------------------------------------------------------------
# Napisz funkcję, która zamieni liczbę w zapisie rzymskim na dziesiętny.

roman_numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_int(roman_number):
    suma = 0
    idx = 0
    while idx < len(roman_number):
        if len(roman_number[idx:]) > 1:
            first = roman_numbers[roman_number[idx]]
            second = roman_numbers[roman_number[idx+1]]
            if first < second:
                suma += second - first
                idx += 2
            else:
                suma += first
                idx += 1
        else:
            suma += roman_numbers[roman_number[idx]]
            idx += 1
    return suma

print(roman_to_int("MCMXCV"))
# --------------------------------------------------------------------
# Stwórz plik txt, wpisz do niego jakąkolwiek treść w notatniku, a następnie
# wyświetl jego zawartość z poziomu kodu Pythona.

open_file = open("Inne pliki/plik_tekstowy.txt", "r")
print(open_file.read())
# --------------------------------------------------------------------
# Spróbuj zapisać wybrany przez siebie cytat do pliku utworzonego w
# poprzednim zadaniu.

open_file = open("Inne pliki/plik_tekstowy.txt", "w")
open_file.writelines("Python is cool")

open_file = open("Inne pliki/plik_tekstowy.txt", "r")
print(open_file.read())
# --------------------------------------------------------------------
# A co gdybyśmy nie chcieli nadpisywać za każdym razem pliku, tylko
# dopisywać coś na jego koniec?

open_file = open("Inne pliki/plik_tekstowy.txt", "a")
open_file.writelines("Python is cool")

open_file = open("Inne pliki/plik_tekstowy.txt", "r")
print(open_file.read())
# --------------------------------------------------------------------
# To teraz wyświetl zawartość wybranego pliku korzystając z poznanego
# słowa kluczowego with

with open("Inne pliki/plik_tekstowy.txt", "w") as f:
    f.write ("Python is cool 2")

with open("Inne pliki/plik_tekstowy.txt", "r") as f:
    print(f.read())
# --------------------------------------------------------------------
# Stwórz plik tekstowy w notatniku, gdzie będzie kilka linii tekstu. Następnie
# odczytaj go w kodzie pythonowym, zamień każde słowo na wielkie litery, a
# następnie zapisz w innym pliku.

with open("Inne pliki/plik_tekstowy_2.txt", "r") as f:
    f = f.read().upper()

with open("Inne pliki/plik_tekstowy_3", "w") as f1:
    f1.write(f)
# --------------------------------------------------------------------
# Sprawdź, czy istnieje plik „pan_tadeusz.txt”, jeśli nie – stwórz go i zapisz
# do niego pierwsze wersy Inwokacji (z pamięci, hihi), a jeśli istnieje -
# wypisz zawartość na ekran. Wszystko z poziomu kodu Pythona.

text = """
    Litwo! Ojczyzno moja! Ty jesteś jak zdrowie,
    Ile cię trzeba cenić, ten tylko się dowie,
    Kto cię stracił. Dziś piękność twą w całej ozdobie
    Widzę i opisuję, bo tęsknię po tobie
    Panno święta, co Jasnej bronisz Częstochowy
"""

import os

if os.path.isfile("Inne pliki/pan_tadeusz.txt"):
    print("Plik już istnieje, a to jego zawartość:")
    with open("Inne pliki/pan_tadeusz.txt", "r") as f:
        print(f.read())
else:
    with open("Inne pliki/pan_tadeusz.txt", "w") as f1:
        f1.write(text)
    print("Dopisano!")