# Using the enumerate() Function with Lists

supplies = ['pens', 'staplers', 'pencils', 'paper', 'binders']

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)



heroes = ['batman', 'superman', 'joker', 'lex luther']

for hero in heroes:
    print(hero)

for villain in enumerate(heroes):
    print(villain)