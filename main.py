# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).
from array import array
from random import randint
from time import time

def heapify(new_array, size_of_array, root_index):
    largest = root_index
    left_value = 2 * root_index + 1
    right_value = 2 * root_index + 2
    if left_value < size_of_array and new_array[root_index] < new_array[left_value]:
        largest = left_value
    if right_value < size_of_array and new_array[largest] < new_array[right_value]:
        largest = right_value
    if largest != root_index:
        new_array[root_index],new_array[largest] = new_array[largest],new_array[root_index]
        heapify(new_array, size_of_array, largest)


def heap_sort(new_array):
    for i in range(len(new_array), -1, -1):
        heapify(new_array, len(new_array), i)
    for i in range(len(new_array) - 1, 0, -1):
        new_array[i], new_array[0] = new_array[0], new_array[i]
        heapify(new_array, i, 0)


def array_gen(min_value, max_value, array_length):
    return [randint(min_value, max_value) for i in range(array_length)]


def time_value(func, x):
    start_time = time()
    returned_value = func(x)
    term_of_action = time() - start_time
    print(f"Выполнено за {term_of_action} секунд.")
    if returned_value is not None:
        return returned_value


my_array = array_gen(0, 1000, 20)
print(my_array)
heap_sort(my_array)
print("Сортированный список: ")
print(my_array)
time_value(heap_sort, my_array)
