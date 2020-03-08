# Stwórz klasę Osoba, która będzie przechowywała imię, nazwisko, wzrost
# oraz wagę. Stwórz kilka jej instancji. Stwórz metodę bmi(), która na podstawie
# informacji o tym indeksie zwróci informację o stanie sylwetki danej osoby.
# Zmodyfikuj klasę Osoba tak, by móc daną osobę wypisać na ekran.

class Osoba:
    def __init__(self, name, lastname, height, weight):
        self.name = name
        self.lastname = lastname
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.lastname}"

    def description(self):
        return f"Imię i nazwisko: {self.name} {self.lastname}"

    def dimensions(self):
        return f"{self.name} ma wzrostu {self.height} cm i waży {self.weight} kg"

    def bmi(self):
        self.height = self.height / 100
        bmi = self.weight / self.height ** 2
        if bmi <= 18.49:
            return f"Twoje BMI wynosi {round(bmi,2)}: Niedowaga"
        elif 18.49 < bmi < 24.50:
            return f"Twoje BMI wynosi {round(bmi,2)}: Waga jest odpowiednia"
        elif 24.99 < bmi:
            return f"Twoje BMI wynosi {round(bmi,2)}: Nadwaga"

tomek = Osoba("Tomasz", "Kowalski", 163, 94)
piotr = Osoba("Piotr", "Nowak", 189, 83)

print(tomek.description())
print(tomek.dimensions())
print(tomek.bmi())
print("\n")
print(piotr.description())
print(piotr.dimensions())
print(piotr.bmi())
print("\n")
print(tomek)
print(piotr)
# --------------------------------------------------------------------
# Stwórz klasę Pracownik, która będzie dziedziczyła po klasie Osoba. Jej
# unikalne pola to: stawka godzinowa oraz liczba godzin przepracowanych
# w miesiącu. Pamiętaj, że chcemy mieć możliwość informowania
# pracownika o jego kondycji na podstawie BMI.

class Pracownik(Osoba):
    def __init__(self, name, lastname, height, weight, worked_hour):
        super().__init__(name, lastname, height, weight)
        self.hourly_rate = 20
        self.worked_hour = worked_hour

    def raportuj_godziny(self):
        obliczenia =  self.hourly_rate * self.worked_hour
        return f"Do wypłaty jest: {obliczenia} zł."


mateusz = Pracownik("Mateusz", "Szczeciniak", 183, 82, 30)
print(mateusz.raportuj_godziny())
print(mateusz.bmi())
# --------------------------------------------------------------------

class Prostokat:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def obwod(self):
        obwod = 2 * (self.height + self.width)
        return f"Obwód wynosi: {obwod}"

    def pole(self):
        pole = self.height * self.width
        return f"Pole prostokąta wynosi: {pole}"

pro1 = Prostokat(10, 10)
pro2 = Prostokat(8.3, 16.34)

print(pro1.obwod())
print(pro1.pole())
print("\n")
print(pro2.obwod())
print(pro2.pole())
# --------------------------------------------------------------------
# Napisz funkcję, która zamieni wartości dwóch zmiennych bez tworzenia
# nowych zmiennych.

def swap(a, b):
    a, b = b, a
    print(" a = %d i b = %d" % (a, b))


a = 30
b = 20
swap(a, b)
# --------------------------------------------------------------------
# Zagraj w „kamień, papier, nożyce” ze swoim komputerem.

import random
print( """
    k - kamień
    p - papier
    n - nożyce
""")

elementy = ["k", "p", "n"]

punkty_czlowiek = 0
punkty_komputer = 0
ilosc = 0

while ilosc < 3:
    czlowiek = input("Podaj znak: ")
    komputer = random.choice(elementy)
    if komputer == "p" and czlowiek == "k" or komputer == "k" and czlowiek == "n" or komputer == "n" and czlowiek == "p":
        punkty_komputer += 1
        ilosc += 1
        print(f"{czlowiek.upper()} v {komputer.upper()}: KOMPUTER WYGRYWA!")
    elif komputer == "k" and czlowiek == "p" or komputer == "n" and czlowiek == "k" or komputer == "p" and czlowiek == "n":
        punkty_czlowiek +=1
        ilosc += 1
        print(f"{czlowiek.upper()} v {komputer.upper()}: CZŁOWIEK WYGRYWA!")
    else:
        ilosc += 0
        print(f"{czlowiek.upper()} v {komputer.upper()}: REMIS!")


if punkty_czlowiek > punkty_komputer:
    print(f"\nCZŁOWIEK WYGRAŁ! {punkty_czlowiek}:{punkty_komputer}")
elif punkty_czlowiek < punkty_komputer:
    print(f"\nKOMPUTER WYGRAŁ! {punkty_komputer}:{punkty_czlowiek}")