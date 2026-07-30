Resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Money": 0}
data = {
    "Espresso": {"Water": 50, "Milk": 00, "Coffee": 18, "Money": 1.50},
    "Latte": {"Water": 200, "Milk": 150, "Coffee": 24, "Money": 2.50},
    "Cappuccino": {"Water": 250, "Milk": 100, "Coffee": 24, "Money": 3.00}
}


def coin_counter():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    money = {"dime": dimes, "quarter": quarters, "nickel": nickles, "penny": pennies}
    total_money = money["dime"] * 0.10 + money["quarter"] * 0.25 + money["nickel"] * 0.05 + money["penny"] * 0.01
    return total_money


def resource_update(f):
    Resources["Water"] -= data[f]["Water"]
    Resources["Milk"] -= data[f]["Milk"]
    Resources["Coffee"] -= data[f]["Coffee"]
    Resources["Money"] += data[f]["Money"]
    return Resources


def report():
    print(f"Water: {Resources['Water']}ml")
    print(f"Milk: {Resources['Milk']}ml")
    print(f"Coffee: {Resources['Coffee']}g")
    print(f"Money: ${Resources['Money']}")

def enough_resources():
    for resource in Resources:
        if resource=="Money" :
            continue
        elif data[flavour][resource] > Resources[resource]:
            print(f"Sorry, you don't have enough {resource}.")
            return False
    return True

coffee_machine = True
while coffee_machine:
    want_coffee = str(input("What would you like? (espresso/ latte/ cappuccino): "))
    if want_coffee.lower() == "off":
        print("Goodbye!")
        coffee_machine = False
    elif want_coffee.lower() == "report":
        report()
    elif want_coffee.lower() in ["espresso", "latte", "cappuccino"]:
        #Checking Resources for different Flavors.
        flavour = want_coffee.capitalize()
        if enough_resources():
            money_inserted = coin_counter()
            money_req = data[flavour]["Money"]
            if money_inserted >= money_req:
                change = round((money_inserted - money_req), 2)
                print(f"Here's ${change} in change.")
                print(f"Here's your {flavour} enjoy!")
                resource_update(flavour)
            else:
                print("Sorry, you don't have enough money. Money refunded.")
    else:
        print("Invalid choice. Please choose espresso, latte, cappuccino, report, or off.")
