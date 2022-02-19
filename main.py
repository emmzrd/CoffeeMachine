MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def remaining_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water:  {water} ml")
    print(f"Milk:   {milk} ml")
    print(f"Coffee: {coffee} mg")
    print(f"Money: $ {profit}")


def coins():
    global should_continue
    print("Please insert coins.")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total_money = round((quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01), 2)
    change = round(total_money - MENU[chosen_beverage]["cost"], 2)
    if total_money < MENU[chosen_beverage]["cost"]:
        print("Insufficient funds.")
        print(total_money)
        should_continue = False
    else:
        print(total_money)
        resources["water"] -= MENU[chosen_beverage]["ingredients"]["water"]
        resources["milk"] -= MENU[chosen_beverage]["ingredients"]["milk"]
        resources["coffee"] -= MENU[chosen_beverage]["ingredients"]["coffee"]
        print(f"Here is your change: {change}")
        print(f"Here is your {chosen_beverage}. Enjoy!")


should_continue = True

while should_continue:

    chosen_beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if chosen_beverage == "report":
        print(remaining_resources())
        chosen_beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()
    elif chosen_beverage == "off":
        should_continue = False
    elif chosen_beverage == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                if resources["milk"] >= MENU["espresso"]["ingredients"]["milk"]:
                    coins()
                    profit += MENU[chosen_beverage]["cost"]
                else:
                    should_continue = False
                    print("Sorry there is not enough milk.")
            else:
                should_continue = False
                print("Sorry there is not enough coffee.")
        else:
            should_continue = False
            print("Sorry there is not enough water.")
    elif chosen_beverage == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                    coins()
                    profit += MENU[chosen_beverage]["cost"]
                else:
                    print("Sorry there is not enough coffee.")
                    should_continue = False
            else:
                print("Sorry there is not enough milk.")
                should_continue = False
        else:
            print("Sorry there is not enough water.")
            should_continue = False
    elif chosen_beverage == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                    coins()
                    profit += MENU[chosen_beverage]["cost"]
                else:
                    print("Sorry there is not enough coffee.")
                    should_continue = False
            else:
                print("Sorry there is not enough milk.")
                should_continue = False
        else:
            print("Sorry there is not enough water.")
            should_continue = False
    else:
        print("You have entered invalid choice.")
