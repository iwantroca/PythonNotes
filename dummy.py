# # dictionary 

# """they are used to store data with keys and values"""

# student_info = {'Name': 'Mohit', 'Age': 34, 'Occupation': 'Rich Boy'}

# print(student_info.get('phone', 'Not Exist'))

# student_info.update({'Name': 'Jane', 'Occupation': 'Designer'})
# print(student_info)


# for k, v in student_info.items():
#     print(k, ":" , v) 

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# # student_info('Art', 'Fashion', name='Jane', age=22)
# courses = ['Art', 'Fashion']
# info = {'name': 'Jane', 'age': 22, 'Occupation': 'Designer'}

# student_info(*courses, **info)

'''Storing days of the month'''
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def day_in_month(year, month):
#     if not 1 <= month <= 12:
#         return 'Invalid Month'
    
#     if is_leap(year) and month == 2:
#         return 29
    
#     return month_days[month]

# print(day_in_month(2020, 2))

# for i in range(10):
#     print(f'the value of num is {i}.')



"""CLASSES"""

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name},{self.age},{self.salary})'

e1 = Employee('Jane', 22, 80000)
e2 = Employee('Aries', 28, 75000)
e3 = Employee('Josh', 28, 79000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort)
print(s_employees)

