# Реализуйте алгоритм перемешивания списка.
def mixing_list(target_list):
    i = 0
    while i < len(target_list) - 1:
        a = target_list[i]
        target_list[i] = target_list[i + 1]
        target_list[i + 1] = a
        i += 2
    return target_list


arr = []
for j in range(10):
    arr.append(j)
print(f"Массив до перемешивания - {arr}")

arr = mixing_list(arr)
print(f"Массив после перемешивания - {arr}")
