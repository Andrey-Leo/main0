def print_params(a=1, b='str', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

values_List = [False, 'Got', 55]
values_dict = {'a':12.25, 'b':12, 'c':'Caramba'}

print_params(*values_List)
print_params(**values_dict)

values_List_2 = ['Grom', 42]

print_params(*values_List_2, 42)
