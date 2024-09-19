def calculate_structure_sum(data_):
    sum_ = 0
    if isinstance(data_, (list, tuple, set)):
        for i in data_:
            sum_ += calculate_structure_sum(i)
    elif isinstance(data_, dict):
        for key, value in data_.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)
    elif isinstance(data_, (int, float)):
        sum_ += data_
    elif isinstance(data_, str):
        sum_ += len(data_)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
