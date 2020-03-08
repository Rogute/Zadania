from abc import ABCMeta, abstractmethod


class Dostawca(metaclass=ABCMeta):

    @abstractmethod
    def oblicz_koszt(self):
        pass


class Fedex(Dostawca):

    def oblicz_koszt(self):
        return 'Dupa'


class Ups(Dostawca):

    def oblicz_koszt(self):
        return 'Dupa1'


class PocztaPolska(Dostawca):

    def oblicz_koszt(self):
        return 'Dupa3'


class Kalkulator:

    def __init__(self, deliver, weight):
        self.deliver = deliver
        self.weight = weight

    def glowne_obliczenie(self):
        if self.deliver is not None:
            self.weight.oblicz_koszt()
        else:
            print('Niepoprawna nazwa')

    def set_deliver(self, deliver):
        self.deliver = deliver


def main():
    wybor1 = Kalkulator('UPS', 10)
    # wybor2 = Kalkulator(None)
    # wybor3 = Kalkulator(None)

    wybor1.glowne_obliczenie()
    # wybor2.do()
    # wybor3.do()

    # wybor1.set_deliver(Ups())
    # wybor1.do()

    # wybor2.set_deliver(PocztaPolska())
    # wybor2.do()
    #
    # wybor3.set_deliver(Fedex())
    # wybor3.do()


if __name__ == '__main__':
    main()
