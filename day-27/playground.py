def add(*args):
    sum = 0 
    for n in args:
        # print(n)
        sum += n
    return sum

print(add(3, 4, 5))