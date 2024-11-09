numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
part_1 = numbers[:4:]
part_2 = numbers[5::]
sum_1 = sum(part_1) + sum(part_2)
numbers_1 = len(numbers)
none = sum_1 / numbers_1
numbers[4] = none
print("Измененный список:", numbers)
