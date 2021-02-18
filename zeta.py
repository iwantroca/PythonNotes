########LISTS########

# assigning the list 
courses = ['History', 'Math', 'Physics', 'CompSci']

# finding length of list
print(len(courses))

# using index in list
print(courses[0])

# adding item to list
courses.append('Art')
print(courses)

# using insert to add in specific location 
courses.insert(2, 'Art')
print(courses) 

# using extend method to add lists
courses_2 = ['Humanities', 'Education']
courses.extend(courses_2)
print(courses)

# removing items from the list
courses.remove('Art') 
print(courses)

# using pop to remove item from the list 

popped = courses.pop()
print(popped)
print(courses)

# to find the index in the list
print(courses.index('Physics'))

# using del to remove specified item
del courses[2] # should delete physics
print(courses)

# to check if item is in list
print('Physics' in courses) 


# to reverse the list
courses.reverse()
print(courses)

# to sort the list
sorted_courses = sorted(courses)
print(sorted_courses)

# list operations on the number
nums = [1, 5, 2, 4, 3]

sorted_nums = sorted(nums)
print(sorted_nums)

print(sum(nums))
print(min(nums))

print("")

# using loop in list
for index,item in enumerate(courses, start=1):
    print(index, item)

# joining the courses with symbol
courses_str = ' - '.join(courses) 
print(courses_str)

# spliting the list
courses_split = courses_str.split(' - ')
print(courses_split)

# tuples are immutable; can't be modified
tuple_1 = ('Art', 'Math', 'Physics')
print(tuple_1[2])  

# tuple don't support list assignment 
# tuple_1[0] = 'Chemistry'

####
######SETS######
####

# to make a empty set 
# empty_set = set() 

# in sets, order of the items do not matter
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}

print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
#####
######Dictionaries######
#####

student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student[1])

# adding new key to the dictionary
student['phone'] = '555-5555'

# using get helps us to change the error for defualt 
print(student.get('phone', 'Not exist'))

print(student)

# updating student dict
student.update({1: 'Jane', 'age': 26})
print(student)

print(student.items()) 

# deleting key in dictionaries
# del student[1] 
student.pop(1)
print(student)

# looping through dictionaries
for key, value in student.items():
    print(key, value) 