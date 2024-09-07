def result(n):
    password = ''
    for i in range(1, n):
        for j in range(2, n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password


n = int(input('Введите число от 3 до 20: '))
print('Пароль: ', result(n))
