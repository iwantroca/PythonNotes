# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __repr__(self):
#         return f'({self.name},{self.age},{self.salary})'


# e1 = Employee('Carl', 37, 70000)
# e2 = Employee('Sarah', 29, 80000)
# e3 = Employee('John', 43, 90000)

# employees = [e1, e2, e3]

# def e_sort(emp):
#     return emp.name 

# s_employees = sorted(employees, key=e_sort)
# print(s_employees) 

tag = 'hl'
text = 'This is a headline'
sentence = f'<{tag}>{text}</{tag}>'
print(sentence)

person = {'name': 'Jenn', 'age': 23}

new_text = f'My name is {person["name"]}.'
print(new_text)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', 33)

class_txt= f'My name is {p1.name} and i am {p1.age} years old.'
print(class_txt)

num = 1000**2
size_txt = f'1 MB is equal to {num:,}'
print(size_txt)