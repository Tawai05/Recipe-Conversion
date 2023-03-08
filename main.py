'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
recipe_name = input("Enter the recipe name: ")
serving_size = int(input("Enter the serving size: "))

ingredients = []

while True:
    ingredient = input("Enter an ingredient (or 'done' to finish): ")
    if ingredient == 'done':
        break
    amount = float(input("Enter the amount needed: "))
    cost_per_unit = float(input("Enter the cost per unit: "))
    ingredients.append((ingredient, amount, cost_per_unit))

total_cost = sum(amount * cost for _, amount, cost in ingredients)
cost_per_serving = total_cost / serving_size

print(f"Recipe Name: {recipe_name}")
print(f"Serving Size: {serving_size}")
print("Ingredients:")
for ingredient, amount, cost_per_unit in ingredients:
    print(f"- {amount} {ingredient} @ ${cost_per_unit:.2f} each")
print(f"Cost Per Serving: ${cost_per_serving:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
