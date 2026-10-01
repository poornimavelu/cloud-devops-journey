#dress_price=(input("what is the budget for your dress gurl?"))
#shoes_price=(input("what is the budget for your shoes gurl?"))
#print("gurl total will be:",dress_price + shoes_price)

dress_price = int(input("what is the budget for your dress gurl? "))
shoes_price = int(input("what is the budget for your shoes gurl? "))

total_outfit = dress_price + shoes_price
print("gurl real total will be:", total_outfit)

# Boolean check: True if 100 or less, False if more
under_budget = total_outfit <= 100
print("Under budget:", under_budget)