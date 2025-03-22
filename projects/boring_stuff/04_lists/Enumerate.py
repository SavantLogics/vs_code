# Using the enumerate() Function with Lists

supplies = ['pens', 'staplers', 'pencils', 'paper', 'binders']

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)



list = ['batman', 'superman', 'joker', 'lex luther']

for hero in list:
    print(hero)

for villain in enumerate(list):
    print(villain)