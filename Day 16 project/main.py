from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker= CoffeeMaker()

is_on=True
while is_on:
    choice= input(f"What would you like? {menu.get_items()}")
    if choice.lower() == "off":
        print("Goodbye!")
        is_on=False
    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)





