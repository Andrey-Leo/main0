def get_multiplied_digits(number):
    str_number = str(number).strip('0')
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
result_1 = get_multiplied_digits(420)
print(result)
print(result_1)
