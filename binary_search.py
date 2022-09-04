def binary_search(list, item):
    low = 0  # мінімальне значення в списку
    high = len(list) - 1  # максимальне значення в списку
    while low <= high:  # допоки ця частина не скоротиться до одного елементу
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:  # значання знайдено
            return guess
        if guess > item:  # Багато
            high = mid - 1
        else:  # Мало
            low = mid + 1
    return None  # Значення не знайдено


my_list = range(1, 129)
print(binary_search(my_list, 128))
