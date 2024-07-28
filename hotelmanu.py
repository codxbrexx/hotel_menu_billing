#Define the manu of restaurant
menu = {
    'pizza': 40,
    'pasta': 50,
    'Burger': 60,
    'salad': 70,
    'coffee': 80,
}

#greet

greet = ("Welcome To HAMARA Restaurant")
print(greet.center(500))
print("Pizza: Rs40\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item {item_2}is not avaialable!")

print(f"The total amount of items to pay is {order_total} ")
