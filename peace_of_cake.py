def get_recipe_price(dic, optionals=None, **ingredients):
    if not dic:
        return 0
    if optionals is not None:
        for op in optionals:
            dic.pop(op)
    sum = 0
    for product, cost in dic.items():
        sum = sum + (ingredients[product]/100)*cost
    return sum


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
