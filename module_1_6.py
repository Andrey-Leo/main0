my_dict = {'Egor': 1994, 'Max': 1991, 'baron': 1972}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Max'])
print('Not existing value: ', my_dict.get('Golem'))
my_dict.update({'Pavel': 1984,
                'Artur': 1978})
print('Deleted value: ', my_dict.pop('Max'))
print('Modified dictionary: ', my_dict)
print( )
my_set = {1,2,3,4, 'Grom', 1,2,3,15}
print('Set: ', my_set)
my_set.add(5)
my_set.add((2,5,8.5))
my_set.remove(15)
print('Modified set: ', my_set)
