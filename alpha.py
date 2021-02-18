def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# student_info('physics', 'math', name='Mohit', age=35)  

courses = ('physics', 'maths') 
info = {'name': 'Mohit', 'age': 32}

student_info(*courses, **info)