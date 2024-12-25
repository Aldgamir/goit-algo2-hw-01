def find_min_max(arr):
    # Базовий випадок: якщо в масиві лише один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # Базовий випадок: якщо два елементи
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Розділяємо масив на дві частини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Знаходимо і повертаємо мінімум і максимум із двох частин
    return (min(left_min, right_min), max(left_max, right_max))


# Приклад масиву для тестування
array = [7, 3, 1, 5, 9, -2, 8, 0, -1, 6, 4, 2, 10]
result = find_min_max(array)
print(f"Мінімальний елемент: {result[0]}, Максимальний елемент: {result[1]}")