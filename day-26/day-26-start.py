num_list = [1, 2, 3, 4, 5]
list_2 = [item + 5 for item in num_list]

name = 'Alvin'
new_list = [i for i in name]

range_list = [num * 2 for num in range(1, 5)]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Freddie']

short_names = [name for name in names if len(name) < 5]

long_names = [name.upper() for name in names if len(name) > 4]

