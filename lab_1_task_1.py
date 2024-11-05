numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_of_elements = sum(num for num in numbers if num is not None)
count_numbers = len(numbers)
average_of_numbers = sum_of_elements / count_numbers
numbers[4] = average_of_numbers
print("Измененный список:", numbers)
