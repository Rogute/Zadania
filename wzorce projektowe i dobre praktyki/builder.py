from abc import ABCMeta, abstractmethod


# class Budynek:
#
#     def __init__(self, drzwi=4, okna=4, dach="Płaski", sciany=4):
#         self.drzwi = drzwi
#         self.okna = okna
#         self.dach = dach
#         self.sciany = sciany
#
#     def __str__(self):
#         return f"Ten budynek posiada {self.drzwi} drzwi, " \
#             f"{self.okna} okien, {self.sciany} scian oraz dach w ksztalcie \'{self.dach}\'"
#
#
# class Builder(metaclass=ABCMeta):
#
#     @abstractmethod
#     def set_drzwi(self, value):
#         pass
#
#     @abstractmethod
#     def set_okna(self, value):
#         pass
#
#     @abstractmethod
#     def set_sciany(self, value):
#         pass
#
#     @abstractmethod
#     def set_dach(self, value):
#         pass
#
#     @abstractmethod
#     def get_budynek(self):
#         pass
#
#
# class Budowanie(Builder):
#
#     def __init__(self):
#         self.budynek = Budynek()
#
#     def set_drzwi(self, value):
#         self.budynek.drzwi = value
#         return self
#
#     def set_okna(self, value):
#         self.budynek.okna = value
#         return self
#
#     def set_sciany(self, value):
#         self.budynek.sciany = value
#         return self
#
#     def set_dach(self, value):
#         self.budynek.dach = value
#         return self
#
#     def get_budynek(self):
#         return self.budynek
#
#
# class BudowanieDirector:
#
#     @staticmethod
#     def construct():
#         builder = Budowanie()
#         model = builder.set_drzwi(5).set_okna(16).set_sciany(15).set_dach("Jednospadowy")
#         return model.get_budynek()
#
# 
# def main():
#     budynek = BudowanieDirector.construct()
#     print(budynek)
#
#
# if __name__ == '__main__':
#     main()

class Kalkulator:
    def __init__