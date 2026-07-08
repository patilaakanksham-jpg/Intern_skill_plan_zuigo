def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average

scores = [85, 90, 78, 92, 88]
print(calculate_average(scores))