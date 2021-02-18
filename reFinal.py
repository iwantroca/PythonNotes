# import random

# msg = ['hello', 'what is your name', 'who are you', 'you mean nothing',
# 'are we alone', 'do you even miss me ?']

# ram = random.randint(0,5)
# print(msg[ram])

birthdays = {
    'Alice': 'Apr 14', 'Mary': 'Sept 22', 'John': 'Dec 1'
}

while True:
    name = input('Input the name.')
    if name == '':
        break
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}.')

    else:
        print(f'we do not have information of bday of {name}.')
        bday = input('Enter the bday here: ')
        birthdays[name] = bday
        print("Birthday database updated.")