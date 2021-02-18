
language = 'Java'


if language == 'Python':
    print('Language is Python')
elif language == 'Java': 
    print('Language is Java')
else:
    print('No Match')

   
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


# if the a and b were 
# differently assigned lists
# then a is b = False  
a = [1, 2, 3]
b = a
print(id(a))
print(a is b)

# if and else condition
# that leads to false are:-
# False, None, Zero, 
# any **empty** list, set or dictionray 
