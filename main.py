MENU = {
   "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
   "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
   "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_ingredient_sufficient(order_ingredients):


    """checking for the sufficiency of the ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"your resources {order_ingredients} arent enough")
            return False
    return True


def process_coins():
    """"returns the total amount based on the coins inserted"""
    print("please insert coins")
    total = int(input("how many quarters? "))*0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickel? ")) * 0.05
    total += int(input("how many penny? "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = (money_received-drink_cost, 2)
        print(f"here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("we cant process your request..not enough money")
        return False


def make_coffee(drink_name, order_ingredients):

    """"take drink name and prepare coffee for the customer"""
    for item in order_ingredients:
        resources["item"] -= order_ingredients["item"]
        print(f"here is your drink {drink_name}")


is_on = True
while is_on:
    choice = input("enter your choice?espresso,latte or cappuccino")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_ingredient_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])





