from pprint import pprint

with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}

    for line in f:
        dish = line.strip()
        recipe = []
        quantity = int(f.readline().strip())
        components = [f.readline().strip().split(" | ") for i in range(quantity)]
        for lines in components:
            ingredient_dict = {'ingredient_name': lines[0],
                               'quantity': int(lines[1]),
                               'measure': lines[2]}
            recipe.append(ingredient_dict)
        cook_book[dish] = recipe
        f.readline().strip()
pprint((cook_book))

def get_shop_list_by_dishes(dishes, person_count):
    spisok_dish = {}
    for dish in dishes:
        if dish in cook_book:
            for name_dish in cook_book[dish]:
                name_dish['quantity'] *= person_count
                if name_dish['ingredient_name'] not in spisok_dish:
                    spisok_dish[name_dish['ingredient_name']] = {'measure': name_dish['measure'], 'quantity': int(name_dish['quantity'])}
                else:
                    spisok_dish[name_dish['ingredient_name']]['quantity'] += int(name_dish['quantity'])
        else:
            print(f'данного блюда {dish} нет в криге рецептов')
    pprint(spisok_dish)

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 5)





