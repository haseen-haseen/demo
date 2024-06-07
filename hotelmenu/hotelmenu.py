Menu = {
    "Pizza": 270,
    "Pasta": 160,
    "Momos": 60,
    "Noodles": 80,
    "Coffee": 40,
    "Sandwich": 50,
    "Burger": 60,
}

print("Welcome To Our Hotel ")
print("Pizza: Rs270\nPasta: Rs160\nMomos: Rs60\nNoodles: Rs80\nCoffee: Rs40\nSandwich: Rs50\nBurger: Rs60\n")

orderItem = 0
item = input("Enter the item you want to order: ")

if item in Menu:
    print(f"Item: {item}")
    orderItem += Menu[item]
    print(f"Your item {item} is added to your order.")
else:
    print(f"The item {item} is not available yet.")

anotherItem = input("Do you want to add another item? (Yes/No): ")

if anotherItem== "yes" or anotherItem== "Yes" :
    item2 = input("Enter the item you want to order: ")
    if item2 in Menu:
        orderItem += Menu[item2]
        print(f"Your item {item2} is added to your order.")
    else:
        print(f"The item {item2} is not available yet.")

print(f"The total order payment is {orderItem}")
