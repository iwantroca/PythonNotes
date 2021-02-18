#####
########STRINGS##########
#####

# hold our message
message = 'hello world'

# prints the message
print(message)

# counts the no of characters
print(len(message))

# using indexing 
print(message[2:])

# converting to upper case
print(message.upper())  

# coutning the certain characters
print(message.count('l'))

# finding the index
print(message.find('world'))

# replacing the message
new_message = (message.replace('world', 'universe'))
print(new_message)

# using slicing 
greeting = 'Hello'
name = 'Michael'
print(f'{greeting}, {name.upper()}. How are you?')

# to find the information about varaiable
print(dir(message))

# to find the information about functions
print(help(str))

#####
#####INTEGERS######
#####

num = 3
print(type(num))

# absolute value of the number
print(abs(-3))

# rounding the number
print(round(2.99, 1))


# converting strings to int
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

# printing the converted ints
print(num_1)
print(num_2)