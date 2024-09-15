def get_multiplied_digits(number):
    str_number = str(number)
    str_number_0 = str_number.rstrip('0')
    first = int(str_number[0])
    if len(str_number_0) > 1:
        return first * get_multiplied_digits(int(str_number_0[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
result_1 = get_multiplied_digits(4200)
print(result)
print(result_1)
