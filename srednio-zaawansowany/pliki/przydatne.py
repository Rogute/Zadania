from random import randint
import timeit


# # --------------------------------------------------------------------
def losowa_lista(ile_znakow=10, przedzial=100):
    random_list = []
    for i in range(0, ile_znakow):
        random_list.append(randint(1, przedzial))

    return random_list


# # --------------------------------------------------------------------
def czas_trwania(fun):
    def new_function(*args, **kwargs):
        start_time = timeit.default_timer()
        fun(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print('Funkcja "{name}" trwała {time} sek.'.format(name=fun.__name__, time=format(elapsed, '.3f')))
        return fun(*args, **kwargs)

    return new_function

# # --------------------------------------------------------------------
