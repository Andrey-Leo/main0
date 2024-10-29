def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы: {number}')
    return result, incorrect_data


def calculate_average(numbers):
    if isinstance(numbers, (int, float)):
        print('В numbers записан некорректный тип данных')
        return None
    elif not isinstance(numbers, (list, tuple)):
        personal_sum(numbers)
        return 0
    else:
        try:
            sum_result, incorrect_data = personal_sum(numbers)
            if incorrect_data == len(numbers):
                return 0
            else:
                return sum_result / (len(numbers) - incorrect_data)
        except ZeroDivisionError:
            return 0



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
