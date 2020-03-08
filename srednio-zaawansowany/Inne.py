def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        argumenty_pozycyjne = ', '.join(str(arg) for arg in args)
        argumenty_nazwane = ', '.join([f'{key} = {value}' for key, value in kwargs.items()])
        print(f'Funkcja {func.__name__}({argumenty_pozycyjne}, {argumenty_nazwane}) zwróciła {result}')
        return result

    return wrapper

@debug
def funk(a, b, c):
    return a + b * c


print(funk(3, b=2, c=4))


def multiply(n):
    def functions(func):
        def wrapper(*args, **kwargs):
            return n * func(*args, **kwargs)

        return wrapper

    return functions


@multiply(20)
def func1():
    return 'Ala ma kota\n'


print(func1())

class IndvisibleIterator:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.i = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.counter == self.n:
            raise StopIteration

        if self.i % self.m != 0:
            self.counter += 1
            return self.i
        return self.__next__()


for i in IndvisibleIterator(10, 3):
    print(i, end=', ')

def indvisible_generator(n, m):
    number = 0
    count = 0
    while count < n:
        if number % m != 0:
            yield number
            count += 1
        number += 1

print()
for i in indvisible_generator(10, 3):
    print(i, end=', ')

import json
import csv
from collections import defaultdict


def loa_data(filename):
    with open('pliki/todos.json') as in_file:
        return json.load(in_file)


def filter_json(data):
    return [task for task in data if task['completed']]


def save_to_csv(data, output_filename):
    header = [key for key in data[0].keys()]
    with open(output_filename, 'w') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow(header)
        for row in data:
            writer.writerow(row.values())


def group_by_users(data):
    users = defaultdict(list)
    for task in data:
        name = 'user_' + str(task.pop('userId'))
        users[name].append(task)
    return users


def save_to_json(data, output_filename):
    with open(output_filename, 'w') as out_file:
        json.dump(data, out_file, indent=2)


data = loa_data('pliki/todos.json')
filtered_data = filter_json(data)
# save_to_csv(data, 'pliki/todo.csv')

user_data = group_by_users(filtered_data)
save_to_csv(user_data, 'todo_users.json')

import re


def is_divisible_by_four(number_str):
    pattern = r'^-?([048]|\d*([02468][048]|[13579][26]))$'
    return bool(re.search(pattern, number_str))


test = ['8', '42', '757465', '2036', '1100', '-12']
for number in test:
    print(number, is_divisible_by_four(number))

import re

text = 'SZczecin TO miasto w POlsce, w wojewodztwie ZAchodniopomorskim, NA PObrzezu Szczecinskim'

pattern_search_long = r'\b[A-Z]{2}[A-Za-z]+\b'
pattern_search_short = r'\b[A-Z]{2}\b'


result = re.sub(pattern_search_long, lambda x: x.group().capitalize(), text)


short_replecaments = re.findall(pattern_search_short, result)
for item in short_replecaments:
    user_answer = input(f'Możliwy błąd: {item}. zy zamienić? (T/N) \n').lower()
    if user_answer == 't':
        result = re.sub(item, item.lower(), result)



print(result)

import logging

logging.basicConfig(filename='pliki/newfile.log', level=logging.WARNING)

logger = logging.getLogger()

logger.setLevel(logging.WARNING)

logger.debug('Debug wiadomość')
logger.info('Tylko informacja')
logger.warning('Ostrzeżenie')
logger.error('Błąd')
logger.critical('Koniec')

import os
import re
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser('Counting python files in the given path')
    parser.add_argument('--dir', '-d', type=str, required=True, help='Path to the directory from witch we would like to count python files')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    counter = 0
    for file in os.listdir(args.dir):
        if re.match(r'.*\.py', file):
            counter += 1

print(counter)

def parse_arguments():
    parser = argparse.ArgumentParser('Liczymy pole trójkąta')
    parser.add_argument('-w', '--wysokosc', help='Podaj wysokosc', type=int, required=True)
    parser.add_argument('-s', '--szerokosc', help='Podaj szerokosc', type=int, required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    print(args.wysokosc * args.szerokosc * 0.5)

def parse_arguments():
    parser = argparse.ArgumentParser('Ile razy wystepuje dany napis')
    parser.add_argument('-d', '--dir', help='Podaj ścieżkę pliku', type=str, required=True)
    parser.add_argument('-n', '--napis', help='Podaj napis', type=str, required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    with open(args.dir) as f:
        pattern = rf'{args.napis}'
        counter = (re.findall(pattern, f.read()).count(pattern))


    print(f'\nW pliku {args.dir} słowo \'{args.napis}\' występuje {counter} razy.')


import logging

logging.basicConfig(filename='pliki/newfile.log', level=logging.WARNING)

logger = logging.getLogger()

logger.setLevel(logging.WARNING)

logger.debug('Debug wiadomość')
logger.info('Tylko informacja')
logger.warning('Ostrzeżenie')
logger.error('Błąd')
logger.critical('Koniec')

import re


def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

if __name__ == '__main__':
    switch = {
        '+': dodawanie,
        '-': odejmowanie,
        '*': mnozenie,
        '/': dzielenie

    }

    user_input = input('Podaj wyrażenie: ')
    pattern = r'(\d+)([\+\-\*/])(\d+)'
    liczba1, dzialanie, liczba2 = re.search(pattern, user_input).groups()

    func = switch[dzialanie]
    print(func(int(liczba1), int(liczba2)))

def switch_day(numer_tygodnia):
    switcher = {
        1: 'Poniedziałek',
        2: 'Wtorek',
        3: 'Środa',
        4: 'Czwartek',
        5: 'Piątek',
        6: 'Sobota',
        7: 'Niedziela'
    }
    return switcher.get(numer_tygodnia, 'LOL')

if __name__ == '__main__':
    user_day = input('Podaj numer tygodnia: ')
    print(switch_day())

from math import sqrt



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"

    def przesun(self, a, b):
        self.x += a
        self.y += b

    def odleglosc(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


if __name__ == '__main__':

    punkt1 = Point(2, 3)
    print(punkt1)

    punkt1.przesun(3, 6)
    print(punkt1)

    punkt2 = Point(2, 5)
    print(punkt2)
    print(punkt1.odleglosc(punkt2))

    punkt3 = punkt1 + punkt2
    print(punkt1 == punkt2)
    print(punkt2 == Point(2, 5))


class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dlugos(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f'Wektor ({self.x}, {self.y}) o dlugosci {self.dlugos()}'

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

if __name__ == '__main__':
    w1 = Wektor(1, 3)
    w2 = Wektor(2, 5)
    w3 = Wektor(4, 5)

    assert str(w3) == 'Wektor (4,3) o długosci 5,6'
    assert w1 + w2 == Wektor(3, 8)
    assert w3.dlugos() == 5.0

    wektor = Wektor(3, 5)
    punkt = Point(3, 5)
    print(wektor == punkt)


class Pies:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f'Pies({self.imie}, {self.wiek})'

    def __repr__(self):
        return f'Pies({self.imie}, {self.wiek})'

    def __gt__(self, other):
        return (self.wiek, len(self.imie), self.imie) >= (other.wiek, len(other.imie), other.imie)


if __name__ == '__main__':
    psy = [Pies('Wacław', 5), Pies('Bujda', 3), Pies('Hektor', 10), Pies('Arnold', 10)]
    print(psy)
    sorted_psy = sorted(psy, key=lambda x: (x.wiek, len(x.imie), x.imie))
    print(sorted_psy)
    sorted_psy2 = sorted(psy)
    print(sorted_psy2)

def func1(pocz, kon):
    lista = []
    for i in range(pocz, kon):
        if i % 7 == 0 and i % 5 != 0:
            lista.append(i)
    return lista


def func2(pocz, kon):
    return [x for x in range(pocz, kon + 1) if not x % 7 and x % 5]


class SposobIterator:
    def __init__(self, pocz, kon):
        self.pocz = pocz - 1
        self.kon = kon

    def __iter__(self):
        return self

    def __next__(self):
        if self.pocz > self.kon:
            raise StopIteration

        self.pocz += 1
        if not self.pocz % 7 and self.pocz % 5:
            return self.pocz
        return self.__next__()


def sposob_generator(pocz, kon):
    for i in range(pocz, kon + 1):
        if not i % 7 and i % 5:
            yield i


zakres = func1(2000, 3000)
for i in zakres:
    print(i, end="; ")

print()

zakres = func2(2000, 3000)
for i in zakres:
    print(i, end="; ")

print()

zakres = SposobIterator(2000, 3000)
for i in zakres:
    print(i, end="; ")

print()

zakres = sposob_generator(2000, 3000)
for i in zakres:
    print(i, end="; ")

import re


def func1(str):
    pattern = r'\w+'
    slowa = re.findall(pattern, str)
    return ', '.join(sorted(slowa, key=lambda x: x.lower()))


string = 'Lorem, ipsum, is, simply, dummy, text, of, the, printing, and, typesetting, industry'

print(func1(string))


def tabliczka(x, y):
    lst = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i * j)
        lst.append(row)
    return lst

def tabliczka2(x, y):
       return [[i * j for j in range(y)] for i in range(x)]


tablica = tabliczka2(20, 20)
for row in tablica:
    print('\t'.join([str(item) for item in row]))

from collections import defaultdict

string = 'Lorem, ipsum, is, simply, dummy, text, of, the, printing, aNd, Typesetting, industry, Lorem, ipsum, is, simply, Dummy, duMMy, text, of, the, printing'


# and, typesetting, industry

def fun1(str):
    lista_slow = [item.strip() for item in str.split(',')]
    dict_forms = defaultdict(list)

    for slowo in lista_slow:
        dict_forms[slowo.lower()].append(slowo)

    unikalne = [value[0] for key, value in dict_forms.items() if len(value) == 1]
    return unikalne


print(fun1(string))

def cyfry_parzyste(number):
    while number > 0:
        if (number % 10) % 2:
            return False
        number = number // 10
    return True

def zwroc_liczby(pocz, kon):
    return [x for x in range(pocz, kon+1) if cyfry_parzyste(x)]


print(cyfry_parzyste(2568))
print(cyfry_parzyste(20024))
print(zwroc_liczby(1000, 3000))
print()
print(1)

def genr1(n):
    for i in range(0, n + 1):
        if i % 7:
            yield i


liczby = genr1(400)
for i in liczby:
    print(i, end=', ')


class SevenIterator:
    def __init__(self, n):
        self.n = n
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.n:
            raise StopIteration

        self.number += 1
        if self.number % 7:
            return self.number
        return self.__next__()


liczby = SevenIterator(200)
for i in liczby:
    print(i, end=', ')

import csv




class Przystanek:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.rozklad = {}

    def __str__(self):
        return f'Przstanek \"{self.nazwa}\"'

    def __repr__(self):
        return f'Przstanek \"{self.nazwa}\"'


class Tramwaj:
    def __init__(self, linia):
        self.linia = linia
        self.przystanki = []

    def __str__(self):
        return f'Tramwaj \"{self.linia}\"'

    def __repr__(self):
        return f'Tramwaj \"{self.linia}\"'


data = []
with open('pliki/dane.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

for d in data:
    print(d)


Utwórz klasę Osoba przyjmującą parametr name i balance. Niezbędna również będzie metoda reprezentacji obiektu oraz metoda
borrow() przyjmującą jakiś obiekt i kwotę jako parametr, aby w razie potrzeby pożyczyć od innej Osoby pieniądze.
Pożyczać pieniądze możesz tylko w przerwie w kursie czyli 11:00 - 11:20 oraz 13:00 - 13:30. Należy to obslużyć dekoratorem.
Uwzględnij, że jeden obiekt może nie mieć pieniędzy aby pożyczyć drugiemu. Przetestuj dzialanie programu tj utwórz
minimum 2 instancje klasy, pożycz pieniadze o ile umozliwia to obecna godzina


class Osoba:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'{self.name} ma na koncie {self.balance}'

    def borrow(self):




dominik = Osoba('Dominik', 20)
print(dominik)


import urllib5
      url = 'https://api.um.warszawa.pl/api/action/datastore_search?resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&limit=5'
      fileobj = urllib.urlopen(url)
      print(fileobj.read())

import urllib.request
with urllib.request.urlopen('https://api.um.warszawa.pl/api/action/datastore_search?resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&limit=5') as response:
   html = response.read()
   print(html)