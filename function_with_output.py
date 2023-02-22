def format_name(f_name, l_name):
    return (f'First name is {f_name} and last name is {l_name}')


x = input('What is your first name?\n').title()
y = input('What is your last name? \n').title()

print (format_name(f_name= x, l_name= y))

