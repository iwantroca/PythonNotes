name = input('Hello what is your name?')
print(f'Hi Mr. {name.upper()}. How are you?')
print(f'{name} is a good name!!')

# trying to show how smart you are
print(f'Your name is {len(name)} characters long') 

# print('What is your age tho?')
age = int(input('What is your age tho?'))

if(age <= 15):
    print('Lul you are a baby :p')
elif(age <= 28):
    print('Yum things might work then')
elif(age > 2000):
    print('I do not want to date some undead hmph')
elif(age > 200):
    print('You are a granny')
else:
    print('ewwwwww!!!!')
