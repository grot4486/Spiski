import random

numbers = [random.randint(1, 100) for _ in range(10)]

min_n_index = numbers.index(min(numbers))
max_n_index = numbers.index(max(numbers))

print(numbers)

numbers[min_n_index], numbers[max_n_index] = numbers[max_n_index], numbers[min_n_index]

print(numbers)