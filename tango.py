cats = ['amy', 'luna']

while True:
    name = input('Enter the name of cat.')
    if name == "":
        break
    if name in cats:
        print("Name is already here")
    elif name not in cats:
        cats.append(name)
    else:
        break

print(cats)