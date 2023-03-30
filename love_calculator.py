# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
lower = names.lower()

t = lower.count('t')
r = lower.count('r')
u = lower.count('u')
e = lower.count('e')
l = lower.count('l')
o = lower.count('o')
v = lower.count('v')
e = lower.count('e')

true = str(t+r+u+e)
love = str(l+o+v+e)
calc = true + love
x = int(calc)


if x < 10 or x > 90:
    print(f'Your score is {x}, you go together like coke and mentos.')
elif x >= 40 and x <= 50:
    print(f'Your score is {x}, you are alright together.')
else:
    print(f"Your score is {calc}. Y'all are Meh!")


