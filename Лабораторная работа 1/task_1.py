numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count = len(numbers)
numbers[4] = 0
summ = sum(numbers)
middle = summ/count
numbers[4] = middle

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
