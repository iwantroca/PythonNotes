# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(my_list[-2:1:-1])

# my_url = 'https://www.google.com'

# print(my_url[12:-4])

nums = [1,2,3,4,5,6,7,8,9,10]

new_list = [num*num for num in nums]
print(new_list)

# new_list = []
# for num in nums: 
#       new_list.append(num*num)
#print(new_list)

even_list = [num for num in nums if num % 2 == 0]
print(even_list)

letter_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(letter_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

hero_list = {name: hero for name, hero in zip(names, heros)if name != 'Peter'}
print(hero_list)

###############################
#Sorting Techniques#############
###############################

tup = (9,1, 8, 3, 4 ,5, 2, 7, 6)
# s_li = sorted(li, reverse=True)
# print(s_li)

s_tup = sorted(tup)
print('Sorted Tuple: ', s_tup)

di = {'name': 'Corey', 'job': 'programming',  'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Sorted Dict\t', s_di) 
