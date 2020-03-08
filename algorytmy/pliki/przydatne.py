from random import randint
from time import clock


# # --------------------------------------------------------------------
def losowa_lista(ile_znakow=10, przedzial=100):
    random_list = []
    for i in range(0, ile_znakow):
        random_list.append(randint(1, przedzial))
    return random_list


# # --------------------------------------------------------------------
def czas_trwania(fun):
    def wrapper(*args, **kwargs):
        start = clock()
        fun(*args, **kwargs)
        end = clock()
        print(format(end - start, '.3f') + ' sek.')
        return fun(*args, **kwargs)

    return wrapper


# # --------------------------------------------------------------------


