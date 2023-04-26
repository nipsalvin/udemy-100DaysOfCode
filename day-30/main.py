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
