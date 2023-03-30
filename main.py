'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

recipe_name = input("Enter the recipe name: ")
serving_size = int(input("Enter the serving size: "))

# create an empty dictionary to store ingredients
ingredients = {}

# prompt the user to add ingredients
while True:
    ingredient_name = input("Enter ingredient name (or 'done' to quit): ")
    if ingredient_name == 'done':
        break
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    ingredients.update({ingredient_name: quantity})
    ingredients.update({ingredient_name: price})

total_cost = sum(info["quantity"] * info["price"] for info in ingredients.values())
cost_per_serving = total_cost / serving_size

print("Ingredients:")
for name, info in ingredients.items():
    quantity = info["quantity"]
    price_per_unit = info["price"]
    print(f"- {quantity} {name} @ ${price_per_unit:.2f} each")
