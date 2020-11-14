message = 'hello world'
new_msg = """bobby's world
is a good cartoon"""

# convert to upper
print(message.upper())
# to find count
print(message.count('l'))
# to find index
print(message.find('world'))
# used to replace
print(message.replace('world','universe'))
# print total count
print(len(new_msg))

# using adding strings
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name
print(message)

## better method 
print(f'{greeting}, {name.upper()}. Welcome !!')

## to find the infomation about variable
# print(dir(name))
# 
## to find the information about functions
# print(help(str))