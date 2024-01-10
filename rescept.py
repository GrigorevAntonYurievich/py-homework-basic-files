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

file_path = 'recipes.txt'  
cook_book = read_recipe_file(file_path)

for recipe, ingredients in cook_book.items():
    print(f'{recipe}:')
    for ingredient in ingredients:
        print(f"  {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
    print()
