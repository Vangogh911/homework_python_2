# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import random


def mul_by_position(position, target_array):
    res = 1
    for j in range(len(position)):
        res *= target_array[position[j]]
    return res


def random_list(count):
    arr = []
    for k in range(count):
        arr.append(int(random() * (count * 2) - count))
    return arr


lines = []
try:
    with open("file.txt", "r") as f:
        for i in f:
            lines.append(int(i))
except FileNotFoundError:
    print("File not found!")

target_arr = random_list(10)
print(f"Целевой массив {target_arr}")
print(f"Позиции {lines}")
print(f"Результат умножения по позициям = {mul_by_position(lines, target_arr)}")
