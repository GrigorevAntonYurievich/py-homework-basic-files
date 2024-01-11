def read_recipe_file(file_path):
    recipes = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            recipe_name = lines[i].strip()
            ingredient_count = int(lines[i + 1].strip())
            
            ingredients = []
            for j in range(ingredient_count):
                ingredient_info = lines[i + 2 + j].strip().split('|')
                ingredient_name = ingredient_info[0].strip()
                quantity = int(ingredient_info[1].strip())
                measure = ingredient_info[2].strip()
                
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(ingredient)
            
            recipes[recipe_name] = ingredients
            i += 2 + ingredient_count
    
    return recipes

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    return shop_list

# Пример использования
file_path = 'recipes.txt'
cook_book = read_recipe_file(file_path)

dishes_to_cook = ['Запеченный картофель', 'Омлет']
person_count = 2
result_shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)

# Выводим полученный словарь
for ingredient, info in result_shop_list.items():
    print(f'{ingredient}: {info["quantity"]} {info["measure"]}')