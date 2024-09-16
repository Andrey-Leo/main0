immutable_var = True, 'Антон', 35, 5.5
print(immutable_var)
#tuple[0] = float - ошибка: объект "тип" не поддерживает назначение элементов
mutable_var = [True, 'Антон', 35, 5.5]
mutable_var.append(immutable_var)
print(mutable_var)