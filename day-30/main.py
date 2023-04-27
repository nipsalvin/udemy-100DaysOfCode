try:
    file = open('file.txt')
    dict = {'key':'value'}
    print(dict['non-key'])
except FileNotFoundError:
    file = open('file.txt', 'w')
    file.write('File created')
except KeyError as error:
    print(f'The key {error}does not exist')
    dict = {'non-key':'non-value'}
    print(dict['non-key'])
else:
    # If there are no exceptions captured
    content = file.read()
    print(content)
finally:
    file.close()
    print('file was closed')


### Raisiing a ValueError ###
height = float(input('Enter Height in meters: '))
weight = float(input('Enter weight in Kgs: '))

if height > 4:
    raise ValueError(f'{height} Meters is too much. Height cannot be over 4 Meters')

bmi = weight/ height **2
print (bmi)


