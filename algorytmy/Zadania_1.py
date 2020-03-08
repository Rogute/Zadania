from pliki.przydatne import losowa_lista


# def common_elements(list1, list2):
#     common_elements_lst = []
#     list2 = set(list2)
#     for elem1 in list1:
#         for elem2 in list2:
#             if elem1 == elem2:
#                 common_elements_lst.append(elem1)
#     return common_elements_lst
#
#
# print(common_elements([1, 2, 3, 3, 4, 5], [3, 4, 6]))


# def get_min_diff(lst):
#     differences = []
#     for i in range(1, len(lst)):
#         differences.append(abs(sum(lst[:i]) - sum(lst[i:])))
#     return min(differences)
#
#
# def get_min_diff2(lst):
#     return min([abs(sum(lst[:i]) - sum(lst[i:])) for i in range(1, len(lst))])
#
#
# def get_min_diff3(lst):
#     differences = []
#     left, right = 0, sum(lst)
#     for elem in lst[:-1]:
#         left += elem
#         right -= elem
#         differences.append(abs(left - right))
#     return differences
#
#
# lst = [3, 1, 2, 4, 3]
#
# print(get_min_diff(lst))
# print(get_min_diff2(lst))
# print(get_min_diff3(lst))

# lst = []
# for i in range(1, 100):
#     lst.append(i)
#
# print(sum(lst))
#
#
# print(sum([i for i in range(1, 100)]))

# def get_sum(lst):
#     return sum(lst)
#
#
# def get_sum1(lst):
#     suma = 0
#     for i in lst:
#         suma += i
#     return suma
#
#
# def get_sum2(lst):
#     return (lst[0] + lst[-1]) / 2 * len(lst)
#
#
# lista = list(range(0, 20, 3))
# print(lista)
#
# print(get_sum(lista))
# print(get_sum1(lista))
# print(get_sum2(lista))


# lst = [25, 1, 2, 3, 45, 3, 4, 5]

# def bubbleSort(lst):
#     for i in range(len(lst) - 1, 0, -1):
#         for i in range(i):
#             if lst[i] > lst[i + 1]:
#                 temp = lst[i]
#                 lst[i] = lst[i + 1]
#                 lst[i + 1] = temp
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubbleSort(lst)
# print(lst)

# lst = [3, 2, 4, 3, 1, 2, 0, 5, 9]


# def SelectSort(lst):
#     for i in range(len(lst)):
#         min_idx = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min_idx]:
#                 min_idx = j
#         lst[i], lst[min_idx] = lst[min_idx], lst[i]
#     return lst
#
#
# print('Selector Sort:', SelectSort(lst))
#
#
# def SelectSort1(lst):
#     for i in range(len(lst)):
#         mini = min(lst[i:])
#         min_index = lst[i:].index(mini)
#         lst[i + min_index] = lst[i]
#         lst[i] = mini
#     return lst
#
#
# print('Selector Sort 1:', SelectSort1(lst))
#
#
# def InsertionSort(lst):
#     for i in range(1, len(lst)):
#         j = i - 1
#         while j >= 0 and lst[i] < lst[j]:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = lst[i]
#     return lst
#
# print('Insertion Sort:', InsertionSort(lst))
#
#
# def InsertionSort1(lst):
#     for idx in range(1, len(lst)):
#         value, pos = lst[idx], idx
#
#         while lst[pos-1] > value and pos > 0:
#             lst[pos] = lst[pos-1]
#             pos -= 1
#         lst[pos] = value
#         print(lst)
#     return lst
#
#
# print('Insertion Sort 1:', InsertionSort1(lst))

# def SortLiniowy(lst, n):
#     idx = 0
#     for i in lst:
#         if i == n:
#             return idx
#         else:
#             idx += 1

# print(lst)
# print(SortLiniowy(lst, 5))

# def SortBinarny(lst, start, end, to_find):
#     if start > end:
#         return -1
#     mid = (start+end) // 2
#     if lst[mid] == to_find:
#         return mid
#     elif lst[mid] > to_find:
#         return SortBinarny(lst, start, mid-1, to_find)
#     return SortBinarny(lst, mid+1, end, to_find)
#
# lst = sorted(lst)
# print(lst)
# print(SortBinarny(lst, 0, len(lst), 4))


# def merge_sort(lst):
#     if len(lst) > 1:
#         mid = len(lst) // 2
#         left, right = lst[:mid], lst[mid:]
#         left, right = merge_sort(left), merge_sort(right)
#
#         i, j, k = 0, 0, 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 lst[k] = left[i]
#                 i += 1
#             else:
#                 lst[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             lst[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             lst[k] = right[j]
#             j += 1
#             k += 1
#     return lst
#

lista = [1, 5, 4, 95, 3, 8, 7, 3]
print(merge_sort(lista))


def quicksort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return lst
    else:
        pivot = lst[0]
        i = 0
        for j in range(len(lst) - 1):
            if lst[j + 1] < pivot:
                lst[j + 1], lst[i + 1] = lst[i + 1], lst[j + 1]
                i += 1
        lst[0], lst[i] = lst[i], lst[0]
        first_part = quicksort(lst[:i])
        second_part = quicksort(lst[i + 1:])
        first_part.append(lst[i])
        return first_part + second_part


lista = [10, 8, 1, 7, 14, 2, 17, 13]
print(quicksort(lista))


def quicksort1(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    left, right = [], []
    for elem in lst[1:]:
        if elem < pivot:
            left.append(elem)
        else:
            right.append(elem)
    return quicksort1(left) + [pivot] + quicksort1(right)


print(quicksort1(lista))


from argparse import ArgumentParser


def sum_swction(lst, start, stop):
    return sum(lst[start:stop + 1])


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--list', '-l', nargs='+', required=True)
    args = parser.parse_args()

    lst = list(map(int, args.list))
    n = int(input('Podaj liczbę przedziałów: '))
    for _ in range(n):
        start, stop = input('Podaj przedział: ').split()
        start, stop = int(start), int(stop)
        print(sum_swction(lst, start, stop))

# lista = losowa_lista(5, 100)
#
#
# def fun(lista):
#     lista = sorted(lista)
#     return lista[0], lista[-1]
#
#
# def find_min_max(lst):
#     min, max = lst[0], lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] < min:
#             min = lst[i]
#         elif lst[i] > max:
#             max = lst[i]
#     return min, max
#
#
def find_min_max2(lst):
    minimum, maximum = lst[0], lst[0]
    n = len(lst)
    is_n_even = False
    if n % 2 == 0:
        n -= 1
        is_n_even = True

    for i in range(1, n, 2):
        if lst[i] > lst[i + 1]:
            current_min, current_max = lst[i + 1], lst[i]
        else:
            current_min, current_max = lst[i], lst[i + 1]

        if current_max > maximum:
            maximum = current_max

        if current_min < minimum:
            minimum = current_min

    if is_n_even:
        if lst[n] > maximum:
            maximum = lst[n]
        elif lst[n] < minimum:
            minimum = lst[n]

    return minimum, maximum


def up_bo(lst):
    n = len(lst)
    op = 0
    for i in range(n):
        has_changed = False
        for j in range(n-1-i):
            op += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                has_changed = True

            if not has_changed:
                break
        print(f'Liczba operacji: {op}')
        return lst


print(lista)
print(fun(lista))
print(find_min_max(lista))
print(find_min_max2(lista))
print(up_bo(lista))

# def brakuje(lst):
#     for i in range(len(lst)):
#         if lst[i] != i:
#             return i
#     return len(lst)
#
#
# def SortBinarny_brakuje(lst, start, end):
#     if start > end:
#         return end + 1
#
#     if start != lst[start]:
#         return start
#
#     mid = (start + end) // 2
#
#     if mid == lst[mid]:
#         return SortBinarny_brakuje(lst, mid + 1, end)
#     return SortBinarny_brakuje(lst, start, mid)
#
#
# def SortBinarny_brakuje2(lst):
#     return SortBinarny_brakuje(lst, 0, len(lst) - 1)
#
#
# lst1 = [0, 1, 2, 6, 9, 11, 15]
# lst2 = [1, 2, 3, 4, 6, 9, 11, 15]
# lst3 = [0, 1, 2, 3, 4, 5, 6]
#
# print(brakuje(lst1))
# print(brakuje(lst2))
# print(brakuje(lst3))
# print()
#
# print(SortBinarny_brakuje2(lst1))
# print(SortBinarny_brakuje2(lst2))
# print(SortBinarny_brakuje2(lst3))


# def find_min_idx(lst, n):
#     for i in range(-1, len(lst)):
#         if lst[i] == n:
#             return i
#         if n not in lst:
#             return -1
#
#
# def find_min_idx_bin(lst, to_find):
#     start, stop = 0, len(lst) - 1
#     result = - 1
#
#     while start <= stop:
#         mid = (start + stop) // 2
#         if lst[mid] == to_find:
#             result = mid
#             stop = mid - 1
#         elif to_find < lst[mid]:
#             stop = mid - 1
#         else:
#             start = mid + 1
#
#     return result
# #
# #
# def find_max_idx_bin(lst, to_find):
#     start, stop = 0, len(lst) - 1
#     result = - 1
#
#     while start <= stop:
#         mid = (start + stop) // 2
#         if lst[mid] == to_find:
#             result = mid
#             start = mid + 1
#         elif to_find < lst[mid]:
#             stop = mid - 1
#         else:
#             start = mid + 1
#
#     return result
#
# def ile_razy(lista, n):
#     ile_razy = 0
#     for i in lista:
#         if i == n:
#             ile_razy += 1
#     return ile_razy
#
#
# def ile_razy_bin(lst, n):
#     max_idx = find_max_idx_bin(lst, n)
#     min_idx = find_min_idx_bin(lst, n)
#     if min_idx == -1:
#         return 0
#     return max_idx - min_idx + 1


# lista = [2, 2, 5, 5, 5, 5, 5, 6, 6, 8, 9, 9, 9]


# print(ile_razy(lista, 5))
# print(ile_razy_bin(lista, 5))

# print(find_min_idx(lista, 5))
# print(find_min_idx_bin(lista, 5))
#
# print(find_min_idx(lista, 4))
# print(find_min_idx_bin(lista, 4))
#
# print(find_max_idx_bin(lista, 5))


# class Stos:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return str(self.stack)
#
#     def is_empty(self):
#         return not self.stack
#
#     def is_full(self):
#         return False
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print('Stos jest pusty')
#             return None


#
#
# stack = Stos()
# stack.push(5)
# stack.push(6)
# stack.push(9)
# stack.push(2)
#
# print(stack)

# class Kolejka:
#     def __init__(self):
#         self.queue = []
#
#     def __str__(self):
#         return str(self.queue)
#
#     def enqueue(self, x):
#         self.queue.append(x)
#
#     def dequeue(self):
#         if not self.empty():
#             self.queue.pop(0)
#             return self.queue
#         else:
#             print("Nie można pobrać elementu z pustej kolejki")
#             return None
#
#     def empty(self):
#         return len(self.queue) == 0
#
#
# kol = Kolejka()
# kol.enqueue(10)
# kol.enqueue(20)
# kol.enqueue(19)
#
# print(kol)
# print(kol.dequeue())
# print(kol.dequeue())
# print(kol.dequeue())


# class Kolejka1:
#     def __init__(self):
#         self.stack1 = Stos()
#         self.stack2 = Stos()
#
#     def enqueue(self, elem):
#         while not self.stack1.empty():
#             self.stack2.push(self.stack1.pop())
#
#         self.stack1.push(elem)
#
#         while not self.stack2.empty():
#             self.stack1.push(self.stack2.pop())
#
#     def dequeue(self):
#         if not self.empty():
#             return self.stack1.pop()
#         else:
#             print("Nie można pobrać elementu z pustej kolejki")
#             return None
#
#     def empty(self):
#         return self.stack1.empty()
#
#
# kolejka = Kolejka1()
# kolejka.enqueue(5)
# kolejka.enqueue(6)
# kolejka.enqueue(9)
#
# print(kolejka.dequeue())
# print(kolejka.dequeue())
# print(kolejka.dequeue())

# class Kolejka:
#     def __init__(self):
#         self.queue = []
#
#     def __str__(self):
#         return str(self.queue)
#
#     def enqueue(self, x):
#         self.queue.append(x)
#
#     def dequeue(self):
#         if not self.empty():
#             self.queue.pop(0)
#             return self.queue
#         else:
#             print("Nie można pobrać elementu z pustej kolejki")
#             return None
#
#     def empty(self):
#         return len(self.queue) == 0
#
#
# class Stos:
#     def __init__(self):
#         self.q1 = Kolejka()
#         self.q2 = Kolejka()
#
#     def empty(self):
#         return self.q1.empty()
#
#     def push(self, item):
#         self.q1.enqueue(item)
#         while not self.q1.empty():
#             self.q2.enqueue(self.q1.dequeue())
#
#         self.q1, self.q2 = self.q2, self.q1
#
#     def pop(self):
#         if not self.empty():
#             return self.q1.dequeue()
#         else:
#             print('Nie można pobrać elementu zpustego stosu')
#             return None
#
#
# if __name__ == '__main__':
#     stack = Stos()
#     stack.push(3)
#     stack.push(5)
#     stack.push(1)
#     stack.push(7)
#     stack.push(2)
#     stack.push(4)
#     stack.push(8)
#
#     print(stack.pop())
#     print(stack.pop())

# class Stos:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return str(self.stack)
#
#     def is_empty(self):
#         return not self.stack
#
#     def is_full(self):
#         return False
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print('Stos jest pusty')
#             return None
#
#
# def expression(symbol, a, b):
#     symbols = {
#         '+': lambda a, b: a + b,
#         '-': lambda a, b: a - b,
#         '*': lambda a, b: a * b,
#         '/': lambda a, b: a / b
#     }
#     func = symbols[symbol]
#     return func(a, b)
#
#
# def calculate(exp_str):
#     stack = Stos()
#     symbols = {'+', '-', '*', '/'}
#     elements = exp_str.split()
#     for elem in elements:
#         if elem in symbols:
#             a = stack.pop()
#             b = stack.pop()
#             result = expression(elem, b, a)
#             stack.push(result)
#         else:
#             stack.push(int(elem))
#     return stack.pop()
#
#
# if __name__ == '__main__':
#     print(calculate('3 5 2 * +'))
#     print(calculate('15 7 1 1 + - / 3 * 2 1 1 + + -'))
#     print(calculate('6 2 3 + - 3 8 2 / + * 2 5 3 + + +'))



