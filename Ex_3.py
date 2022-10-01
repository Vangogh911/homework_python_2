# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input("Введите число: "))
arr = []
for i in range(num):
    arr.append(round((1 + 1/(i+1))**(i+1), 2))
print(arr)
print(f"Сумма чисел последовательности = {round(sum(arr), 2)}")
