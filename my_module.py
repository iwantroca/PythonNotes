print('Importing my_module....')

test = 'Test String'

def find_index(to_find, target):
    for i, value in enumerate(to_find):
        if value == target:
            return i
    
    return -1
