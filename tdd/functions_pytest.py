def is_odd(data):
    return data % 2 != 0


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return


class Dog(Animal):
    def speak(self):
        return "Hau!"


class Cat(Animal):
    def speak(self):
        return 'Miau!'


import requests


def is_correct_website(url):
    req = requests.get(url)
    return 200 <= req.status_code < 400
