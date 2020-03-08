from pliki.przydatne import losowa_lista, czas_trwania
import re
import argparse
import os


# --------------------------------------------------------------------
# Napisz program, który zapyta użytkownika o rok jego urodzenia, a
# następnie zwróci informację o tym, czy jest pełnoletni. Program powinien
# być idiotoodporny.

import datetime


def pelnoletni(rok):
    obecny_rok = datetime.datetime.now().year
    try:
        rok = int(rok)
        if obecny_rok - rok >= 18:
            print("Jesteś pełnoletni")
        else:
            print("Jesteś niepełnoletni")
    except ValueError:
        print("Wpisz same liczby całkowite")


pytanie = input("Podaj swój rok urodzenia: ")
pelnoletni(pytanie)
# --------------------------------------------------------------------
# Napisz program, który zapyta użytkownika o nazwę miesiąca, a następnie
# zwróci informację, ile dany miesiąc ma dni. Program powinien być
# idiotoodporny.

miesiace = {
    'Styczeń': 31,
    'Luty': 29,
    'Marzec': 31,
    'Kwiecień': 30,
    'Maj': 31,
    'Czerwiec': 30,
    'Lipiec': 31,
    'Sierpień': 31,
    'Wrzesień': 30,
    'Październik': 31,
    'Listopad': 30,
    'Grudzień': 31
}


def ile_dni(miesiac):
    if miesiac in miesiace:
        return miesiace.get(miesiac)
    else:
        return 'Miesiąc nie istnieje'


pytanie = input("Podaj nazwę miesiąca: ")
print(ile_dni(pytanie))


# --------------------------------------------------------------------
# Napisz program, który wypisze na ekran zawartość pliku, którego nazwę
# podaje użytkownik.

def fun_open():
    pytanie = input('Podaj nazwę pliku: ')
    nazwa_pliku = 'pliki/' + pytanie

    try:
        with open(nazwa_pliku, 'r') as w_pliku:
            return w_pliku.read()
    except FileNotFoundError:
        print('Plik nie istnieje, podaj jeszcze raz:')
        return fun_open()


print(fun_open())


# --------------------------------------------------------------------
# Napisz program, który zwróci wartość bezwzględną liczby pobranej od
# użytkownika. Program powinien pytać o tę liczbę tak długo, aż nie
# zostanie ona poprawnie podana.


def liczba_bewzgledna():
    try:
        n = int(input('Podaj dowloną liczbę całkowitą: '))
        if n == 0:
            return 'Wartość bewzględna wynosi: 0'
        elif n < 0:
            return f'Wartość bewzględna wynosi: {n * -1}'
        elif n > 0:
            return f'Wartość bewzględna wynosi: {n}'
    except ValueError:
        return liczba_bewzgledna()


print(liczba_bewzgledna())
# --------------------------------------------------------------------
# Napisz program, który obliczy pole trójkąta na podstawie podanych przez
# użytkownika długości podstawy oraz wysokości, pod warunkiem, że obie
# te liczby są dodatnie.

def pole_trojkata():
    wysokosc = float(input('Podaj wysokość trójkąta: '))
    szerokosc = float(input('Podaj szerokość trójkąta: '))
    if wysokosc < 0 or szerokosc < 0:
        raise ValueError('Nie może być poniżej zera!')
    pole = 0.5 * wysokosc * szerokosc
    return pole


print(pole_trojkata())
# --------------------------------------------------------------------
# Zmodyfikuj poprzednie zadanie, tworząc swój własny wyjątek.
class Mniej_niz_zero(Exception):
    def __init__(self):
        message = 'Liczba nie może być poniżej zera'
        super().__init__(message)


def pole_trojkata():
    wysokosc = float(input('Podaj wysokość trójkąta: '))
    szerokosc = float(input('Podaj szerokość trójkąta: '))
    if wysokosc < 0 or szerokosc < 0:
        raise Mniej_niz_zero
    pole = 0.5 * wysokosc * szerokosc
    return pole


print(pole_trojkata())
# --------------------------------------------------------------------
# Stwórz program, który pobiera od użytkownika liczbę z zakresu od 1 do
# 100 i losuje drugą, z zakresu od -5 do 5, a następnie dzieli pierwszą przez
# drugą. Pamiętaj o odpowiedniej obsłudze niepożądanych działań.

from random import randint


class Zakres(Exception):
    def __init__(self):
        message = 'Liczba musi być w przedziale od 1 do 100'
        super().__init__(message)


class Mniej_niz_zero(Exception):
    def __init__(self):
        message = 'Liczba nie może być poniżej zera'
        super().__init__(message)


def zakres(n):
    if 0 < n < 101:
        return n
    else:
        raise Zakres


def dzielenie(n):
    losowa = randint(-5, 5)
    print(losowa)
    if losowa == 0:
        raise Mniej_niz_zero
    else:
        return n / losowa


liczba_uzytkownika = int(input('Podaj liczbę całkowitą w zakresie od 1 do 100: '))

print(dzielenie(zakres(liczba_uzytkownika)))
# --------------------------------------------------------------------
# Przy pomocy funkcji reduce znajdź w liście element największy.
from functools import reduce

lst = [1, 435, 2, 43, 184, 3, 4, 980, 5, 0, -17, 1459]

print(reduce((lambda x, y: x if x > y else y), lst))
# --------------------------------------------------------------------
# Napisz funkcję, która jako argument przyjmuje listę, a zwraca listę
# sześcianów elementów listy wejściowej. Trzema sposobami.

lst = [1, 435, 2, 43, 184, 3, 4, 980, 5, 0, -17, 1459]


def iter(lista):
    nowa_lista = []
    for i in lista:
        return nowa_lista.append(i ** 3)
    return nowa_lista


print(iter(lst))


def compr(lista):
    return [i ** 3 for i in lista]


print(compr(lst))

print(list(map(lambda x: x ** 3, lst)))
# --------------------------------------------------------------------
# Napisz funkcję, która zwraca listę wszystkich niepodzielnych przez 3 liczb
# z zakresu [1, 100]. Trzema sposobami.

zakres = range(0, 101)


def iter(zakres):
    nowa_lista = []
    for i in zakres:
        if i % 3 != 0:
            nowa_lista.append(i)
    return nowa_lista


print(iter(zakres))


def compr(zakres):
    return [i for i in zakres if i % 3 != 0]


print(compr(zakres))

print(list(filter(lambda x: x % 3 != 0, zakres)))
# --------------------------------------------------------------------
# Napisz funkcję, która przyjmuje dwa parametry: jednym jest lista, a drugim
# liczba całkowita z domyślną wartością równą 5. Powinna zwracać listę
# tych elementów, które nie przekroczyły wartości tego parametru. Trzema
# sposobami.

liczba = 5
lst = [1, 435, 2, 43, 184, 3, 4, 980, 5, 0, -17, 1459]


def iter(liczba, lista):
    nowa_lista = []
    for i in lista:
        if i <= liczba:
            nowa_lista.append(i)
    return nowa_lista


print(iter(liczba, lst))


def compr(liczba, lista):
    return [i for i in lista if i <= liczba]


print(compr(liczba, lst))

print(list(filter(lambda x: x <= liczba, lst)))
# --------------------------------------------------------------------
# Napisz funkcję, która przyjmuje listę i zwraca ją w zmienionej formie: tam,
# gdzie liczba była parzysta teraz mamy napis „Parzysta”, a tam, gdzie
# nieparzysta – (niespodzianka) „Nieparzysta”. Trzema sposobami.

lst = [1, 435, 2, 43, 184, 3, 4, 980, 5, 0, -17, 1459]


def iter(lista):
    nowa_lista = []
    for i in lista:
        if i % 2 == 0:
            nowa_lista.append('Parzysta')
        elif i % 2 != 0:
            nowa_lista.append('Nieparzysta')
    return nowa_lista


print(iter(lst))


def compr(lista):
    return ['Parzysta' if i % 2 == 0 else 'Nieparzysta' for i in lista]


print(compr(lst))

print(list(map(lambda x: 'Parzysta' if x % 2 == 0 else 'Nieparzysta', lst)))
# --------------------------------------------------------------------
# Napisz funkcję, która przyjmuje listę i zwraca sumę kwadratów parzystych
# elementów. Trzema sposobami.

lst = [1, 435, 2, 43, 184, 3, 4, 980, 5, 0, -17, 1459]


def iter(lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i ** 2
    return suma


print(iter(lst))


def compr(lista):
    return sum([i ** 2 for i in lista if i % 2 == 0])


print(compr(lst))

parzyste = list(filter(lambda x: x % 2 == 0, lst))
print(sum(list(map(lambda x: x ** 2, parzyste))))
# --------------------------------------------------------------------
# Napisz funkcję, która jako argument przyjmuje listę, a zwraca listę
# sześcianów elementów listy wejściowej. Trzema sposobami.

lst = [1, 435, 2, 43, 184, 3, 4, 980, 5, 0, -17, 1459]


def iter(lista):
    nowa_lista = []
    for i in lista:
        nowa_lista.append(i ** 3)
    return nowa_lista


print((iter(lst)))


def compr(lista):
    return [i ** 3 for i in lista]


print(list(map(lambda x: x ** 3, lst)))

print(compr(lst))
# --------------------------------------------------------------------
# Stwórz listę z 10 losowymi wartościami z przedziału [-10; 10], a następnie
# posortuj ją rosnąco pod względem kwadratów elementów

from random import randrange

lst = [randrange(-10, 10) for _ in range(10)]

print(sorted(lst, key=lambda x: x ** 2))


# --------------------------------------------------------------------
# Stwórz funkcję, która przyjmuje listę napisów i zwraca ją w postaci
# posortowanej, od najkrótszego do najdłuższego.

def sortowanie(lista):
    lista.sort(key=len)
    return lista


lst = ['3klamka', '4komputer', '2hasło', '1dżem']

print(sortowanie(lst))
# --------------------------------------------------------------------
# Udekoruj dowolną nieprzyjmującą argumentów funkcję z poprzednich
# zajęć, dodając informację przed jej wykonaniem „START” oraz „STOP” po
# wykonaniu.Udekoruj dowolną funkcję zwracającą jakąś wartość, tak, by możliwe
# było badanie czasu jej wykonania.

import time


def start_stop(funk):
    def wrapper():
        print('START')
        start = time.clock()
        print(funk())
        print('STOP')
        stop = time.clock()
        return format(stop - start, '.5f') + ' sekund'
    return wrapper


@start_stop
def pole_trojkata():
    wysokosc = 10
    szerokosc = 10
    if wysokosc < 0 or szerokosc < 0:
        raise ValueError('Nie może być poniżej zera!')
    pole = 0.5 * wysokosc * szerokosc
    return pole


print(pole_trojkata())
# --------------------------------------------------------------------
Zastanów się, co należy zmienić, by możliwe było udekorowanie dowolnej
funkcji, nawet takiej, która przyjmuje dowolną liczbę argumentów.

def start_stop(funkcja):
    def wrapper(*args, **kwargs):
        print("START")
        results = funkcja(*args, **kwargs)
        print(results)
        print("STOP \n")

    return wrapper


@start_stop
def sortowanie(lista):
    lista.sort(key=len)
    return lista

lst = ['3klamka', '4komputer', '2hasło', '1dżem']

sortowanie(lst)
# --------------------------------------------------------------------
# Napisz dekorator, który spowoduje, że przy wywołaniu udekorowanej
# funkcji wypisze się na ekran informacja po raz który ta funkcja jest
# wywoływana, np.: "Funkcja <nazwa funkcji> została uruchomiona <n>
# raz"

def wyw(funkcja):
    cache = {}

    def wrapper(*args, **kwargs):
        cache[funkcja.__name__] = cache.get(funkcja.__name__, 0) + 1
        print(f'Funkcja {funkcja.__name__} została wywołana {cache[funkcja.__name__]} razy.')
        return funkcja(*args, **kwargs)

    return wrapper


@wyw
def dowolna_funkcja():
    return 'Wywołuję funkcję'

print(dowolna_funkcja())
print(dowolna_funkcja())
# --------------------------------------------------------------------
# Stwórz funkcję wyświetlającą na ekranie dowolny napis, a następnie
# dekorator, który będzie wykonywał tę funkcję n razy (gdzie n jest
# parametrem przekazywanym do dekoratora).


def wiele_razy(n=1):
    def real_wrapper(fun):
        def wrapper():
            for x in range(n):
                fun()
        return wrapper
    return real_wrapper


@wiele_razy(5)
def wyswietl_napis():
    print ('Wyświetlam dowolny napis')


wyswietl_napis()
# --------------------------------------------------------------------
# Napisz dekorator, który będzie wymagał podania hasła przed właściwym
# wywołaniem funkcji. Jeśli zostanie podane błędne hasło to niech będzie
# wypisany komunikat o braku dostępu.

def daj_password(fun):
    haslo_uzytkownika = input('Podaj hasło: ')

    def wrapper():
        if haslo_uzytkownika == 'dupa':
            return fun()
        else:
            return 'Brak wejścia!'

    return wrapper


@daj_password
def srodek():
    return 'Witamy w środku!'


print(srodek())
# --------------------------------------------------------------------
# Stwórz plik CSV, w którym zapiszesz informacje o tym, kto pracuje w
# Twojej firmie i ile miesięcznie zarabia. Następnie odczytaj ten plik w
# kodzie pythonowym (nazwa pliku niech będzie przekazywana przez
# input), przyznaj każdemu 10% podwyżki i zapisz nową pensję jako
# kolejną kolumnę w nowym pliku CSV.

import csv

nazwa_pliku = 'pracownicy' # input('Podaj nazwę pliku bez rozszerzenia: ')

try:
    with open(f'pliki/{nazwa_pliku}.csv') as odczyt, \
            open(f'pliki/{nazwa_pliku}3.csv', 'w', newline='') as zapis:
        reader = csv.reader(odczyt)
        writer = csv.writer(zapis)
        for idx, row in enumerate(reader):
            print(idx, row)
            if idx == 0:
                row.append("pensja po podwyżce")
                print(row, '\n')
            else:
                row.append(int(row[-1]) * 1.10)
                print(row, '\n')
            writer.writerow(row)

except FileNotFoundError:
    print('Plik nie istnieje!')
# --------------------------------------------------------------------
# Stwórz plik JSON, w którym zapiszesz informacje o tym, kto pracuje w
# Twojej firmie i ile miesięcznie zarabia. Następnie odczytaj ten plik w
# kodzie pythonowym (nazwa pliku niech będzie przekazywana przez
# input), przyznaj każdemu 10% podwyżki i zapisz nową pensję jako
# kolejną wartość w nowym pliku JSON.

import json

nazwa_pliku = 'pracownicy' # input('Podaj nazwę pliku bez rozszerzenia: ')

try:
    with open(f'pliki/{nazwa_pliku}.json') as odczyt, open(f'pliki/{nazwa_pliku}3.json', 'w') as zapis:
        data = json.load(odczyt)

        for row in data:
            row['nowa pensja'] = row['pensja'] * 1.1

        json.dump(data, zapis, indent=2)
        for row in data:
            print('Pracownik: ' + row['pracownik'])
            print('Pensja: ' + str(row['pensja']))
            print('Nowa pensja: ' + str(row['nowa pensja']) + '\n')
except FileNotFoundError:
    print('Podany plik nie istnieje!')
# --------------------------------------------------------------------
# Napisz iterator i generator zwracające sumę składaną, tj. sumę liczb od 1
# do n, gdzie n podawane jest jako wartość końcowa jako parametr.
# gdy n = 10: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

class SumIterator:
    def __init__(self, n):
        self.n = n
        self.current_sum = 0
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        self.current_sum += self.i
        return self.current_sum


for i in SumIterator(10):
    print(i)

def SumGen(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
        yield suma


for i in SumGen(10):
    print(i)
# --------------------------------------------------------------------
# Napisz iterator i generator zwracające kwadrat danej liczby
# gdy n = 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

class KwaIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i ** 2


for i in KwaIter(10):
    print(i)


def kwa_generator(n):
    for i in range(1, n + 1):
        suma = i ** 2
        yield suma


for i in kwa_generator(10):
    print(i)


def sum_generator(n):
    suma = 0
    for q in range(1, n + 1):
        suma += q
        yield suma


for i in sum_generator(10):
    print(i)
# --------------------------------------------------------------------
# Stwórz wyrażenie regularne, które pozwoli wyszukać w dowolnym tekście
# wszystkie zawarte w nim adresy e-mail. Np. „Kamil kamil@google.com, Tomek tomek@o2.pl'”

def znajdz_mail(tekst):
    pattern = r'\w+@\w+\.\w+'
    szukaj = re.findall(pattern, tekst)
    return szukaj


string = 'Kamil kamil@google.com, Tomek tomek@o2.pl'

print(znajdz_mail(string))
# --------------------------------------------------------------------
# Przy wykorzystaniu funkcji re.search dokonaj usunięcia z poniższego adresu e-mail stwierdzenia
# 'remove_this': jan@onremove_thiset.pl. Efektem końcowym powinien być adres jan@onet.pl

def remove_this(tekst):
    pattern = 'remove_this'
    start, stop = re.search(pattern, tekst).span()
    return string[:start] + string[stop:]


string = 'jan@onremove_thiset.pl'

print(remove_this(string))
# --------------------------------------------------------------------
# Przy wykorzystaniu funkcji re.sub w dowolnie napisanym przez Ciebie
# zdaniu zacenzuruj jego część na '*'

string = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the ' \
         'industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ' \
         'scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap ' \
         'into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with ' \
         'the release of Letraset sheets containing lorem Ipsum passages, and more recently with desktop ' \
         'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'


def wykropkuj(tekst):
    pattern = r'[L-l]orem'
    match = re.search(pattern, tekst)
    if match:
        start, stop = match.span()
        zamien = re.sub(pattern, '*' * (stop - start), tekst)
        return zamien

print(wykropkuj(string))
# --------------------------------------------------------------------
# Wypisz wszystkie wyrazy o długości mniejszej niż 6 ze zdania „Nie lubię w
# poniedziałki wcześnie wstawać”

def mniej_niz_6(tekst):
    pattern = r'\b\w{1,6}\b'
    return re.findall(pattern, tekst)


string = 'Nie lubię w poniedziałki wcześnie wstawać'

print(mniej_niz_6(string))
# --------------------------------------------------------------------
# Załóżmy, że poprawny numer telefonu składa się z 9 cyfr i zaczyna od 7,
# 8 lub 9. Napisz funkcję, która sprawdzi, czy numer telefonu przekazany
# przez użytkownika jest poprawny.

def numer_telefonu(number):
    number = number.replace('-', '')
    pattern = r'[7-9]\d{8}'
    sprawdz = re.fullmatch(pattern, number)
    if sprawdz:
        return 'Numer jest poprawny'
    return 'Numer jest niepoprawny'


print(numer_telefonu('123456789'))
print(numer_telefonu('789123123'))
print(numer_telefonu('893652845'))
print(numer_telefonu('906348273'))
print(numer_telefonu('80347543'))
print(numer_telefonu('9736456363'))
print(numer_telefonu('973-645-636'))
print(numer_telefonu('273-645-636'))
print(numer_telefonu('734-645-63'))
# --------------------------------------------------------------------
# Wypisz wszystkie wyrazy rozpoczynające się na ‘a’ lub ‘e’ z dowolnego
# napisu.

string = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the ' \
         'industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ' \
         'scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap ' \
         'into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with ' \
         'the release of Letraset sheets containing lorem Ipsum passages, and more recently with desktop ' \
         'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'


def a_lub_e(tekst):
    pattern = r'\b[a|e]\w+'
    return re.findall(pattern, tekst)


print(a_lub_e(string))
# --------------------------------------------------------------------
# Wypisz wszystkie ciągi więcej niż dwóch samogłosek z tekstu.
# Na przykład dla napisu: „rabcdeefgyYhFjkIoomnpOeorteeeeet”
# poprawna odpowiedź to: [„ee”, „yY”, „Ioo”, „Oeo”, „eeeee”]

def samoglowski(tekst):
    pattern = r'[aeyioąęuó]{2,}'
    return re.findall(pattern, string, re. I)


string = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'

print(samoglowski(string))
# --------------------------------------------------------------------
# Korzystając z wyrażenia regularnego napisz funkcję, która sprawdzi, czy
# liczba jest podzielna przez 4.

def podzielna_4(liczba):
    liczba = str(liczba)
    pattern = r'\d+[2,6,8]'
    sprawdz = re.fullmatch(pattern, liczba)
    if sprawdz:
        return 'Liczba jest podzielna przez 4'
    return 'Liczba nie jest podzielna przez 4'


print(podzielna_4(123))
print(podzielna_4(4892))
print(podzielna_4('16'))
# --------------------------------------------------------------------
# Z daty w postaci YYYY-MM-DD wyekstrahuj do osobnych zmiennych
# dzień, miesiąc i rok.

def rozklad_daty(data):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    rok, miesiac, dzien = re.search(pattern, data).group(1), re.search(pattern, data).group(2), re.search(pattern, data).group(3)
    return rok, miesiac, dzien

print(rozklad_daty('1923-12-28'))
# --------------------------------------------------------------------
# Typowym błędem przy szybkim wpisywaniu tekstu jest pisanie drugiej litery
# wyrazu dużą literą, np. SZczecin (zamiast Szczecin) czy POlska (zamiast
# Polska). Napisz program, wykorzystujący funkcję sub i wyrażenia regularne,
# który poprawi wszystkie takie błędy w tekście wprowadzonym przez
# użytkownika. Wyrazy dłuższe niż dwie litery mają być poprawiane
# automatycznie, natomiast o podmianę wyrazu dwuliterowego (np. IT na It)
# program ma pytać użytkownika za każdym razem, gdy na taki natrafi.


string = 'POlska, SZczecin, IT, It, Polska, Warszawa, WArszawa'

pattern = r'[A-Z]{2}\w*'
szukaj = re.findall(pattern, string)
for i in szukaj:
    if len(i) > 2:
        print(i.capitalize())
    elif len(i) < 3:
        zapytanie = input(f'Czy obecną formę "{i}" zamienić na "{i.capitalize()}" [T lub N] ').upper()
        if zapytanie == 'T':
            print(i.capitalize())
        elif zapytanie == 'N':
            print(i)
# --------------------------------------------------------------------
# Stwórz skrypt, który zwróci pole trójkąta dla długości podstawy i wysokości
# przekazanych jako argumenty w konsoli poleceń.

def argumenty_parsowania():
    parser = argparse.ArgumentParser('Obliczenie pola trójkąta')
    parser.add_argument('-w', '--wysokosc', type=int, required=True, help='Podaj wysokość trójkąta')
    parser.add_argument('-d', '--dlugosc', type=int, required=True, help='Podaj wługość trójkąta')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = argumenty_parsowania()
    pole = 0.5 * args.dlugosc * args.wysokosc
    print(pole)
# --------------------------------------------------------------------
Stwórz skrypt, w którym przekażesz ścieżkę do pliku tekstowego oraz napis,
którego liczbę wystąpień w tym pliku chcesz poznać.

def argumenty_parsowania():
    parser = argparse.ArgumentParser('Policz wystąpienia danego słowa w danym pliku')
    parser.add_argument('-d', '--dir', type=str, required=True, help='Podaj scieżkę pliku')
    parser.add_argument('-s', '--slowo', type=str, required=True, help='Podaj słowo')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argumenty_parsowania()
    args.slowo = args.slowo.lower()
    counter = 0
    with open (args.dir) as in_file:
        reader = in_file.read().lower().split()
        for i in reader:
            if i == args.slowo:
                counter += 1
    print(counter)
# --------------------------------------------------------------------
# Stwórz kalkulator, który na podstawie pobranych od użytkownika dwóch liczb
# oraz znaku między nimi komputer wykona odpowiednie działanie,

def mnozenie(liczba1, liczba2):
    return liczba1 * liczba2

def dzielenie(liczba1, liczba2):
    return liczba1 / liczba2

def dodawanie(liczba1, liczba2):
    return liczba1 + liczba2

def odejmowanie(liczba1, liczba2):
    return liczba1 - liczba2

def kalkulator(liczba1, liczba2, znak):
    liczba1, liczba2 = int(liczba1), int(liczba2)
    kalk = {
        '*': mnozenie(liczba1, liczba2),
        '/': dzielenie(liczba1, liczba2),
        '+': dodawanie(liczba1, liczba2),
        '-': odejmowanie(liczba1, liczba2)
    }
    return kalk.get(znak, 'Błąd składni')


pytanie1 = input('Podaj pierwszą cyfrę: ')
pytanie2 = input('Podaj drugą cyfrę: ')
znak = input('Podaj rodzaj działania (* / - +) ')

print(kalkulator(pytanie1,pytanie2,znak))
# --------------------------------------------------------------------
# Napisz program do zamiany numeru dnia tygodnia na jego nazwę.

def tydzien(numer):
    tydz = {
        1: 'Poniedziałek',
        2: 'Wtorek',
        3: 'Środa',
        4: 'Czwartek',
        5: 'Piątek',
        6: 'Sobota',
        7: 'Niedziela'
    }
    return tydz.get(numer, 'Nie ma takiego dnia!')

print(tydzien(5))
