
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
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Desculpa, não temos {item}. ")
            return False
    return True

def process_coins():
    """Return true when it is enough and false on the contrary"""
    print("Por favor, insira moedas.")
    total = int(input("Quantas quarters: ")) * 0.25
    total += int(input("Quantas dimes: ")) * 0.1
    total += int(input("Quantas nickes?: ")) * 0.05
    total += int(input("Quantas pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """True when payment is accepted, False if it is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aqui está ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Dinheiro insuficiente")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui está o seu {drink_name} ")

is_on = True
while is_on:
    choice = input("O que você gostaria? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['water']}ml")
        print(f"Coffe: {resources['milk']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])


