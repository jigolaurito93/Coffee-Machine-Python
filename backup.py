from menu import MENU, resources
import math

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]



espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# Flag to indicate that coffee machine is off or on
machine_off = False
money_inside = False

# Start While Loop Here
# =================================================================
while not machine_off:

    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    response = input(f"  What would you like? (espresso/latte/cappuccino): ").lower()
    # print(response)

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # Input "off" to turn off coffee machine (secret word)
    # if response == "off":
    #     machine_off = True

    # 3. Print report.
    # When user enters "report", it should show the current resource values
    # Function that prints the current resource values

    def print_report(resources):
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g")
        if money_inside:
            print(f"Money: {cost}")
            
    # If you type "report" as response, it will print the resource values
    if response == "report":
        print_report(resources)


    # 4. Check resources sufficient?

    # Espresso
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

    if response == "espresso":
        if espresso_water > water:
            print(f"Sorry there is not enough water.")
        elif espresso_water < water:
            if espresso_coffee > coffee:
                print(f"Sorry there is not enough water.")
            elif espresso_coffee < coffee:
                water -= espresso_water
                coffee -= espresso_coffee
                cost = espresso_price

    # Latte
    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]

    if response == "latte":
        if latte_water > water:
            print(f"Sorry there is not enough water.")
        elif latte_water < water:
            if latte_milk > milk:
                print(f"Sorry there is not enough milk.")
            elif latte_milk < milk:
                if latte_coffee > coffee:
                    print(f"Sorry there is not enough coffee.")
                elif latte_coffee < coffee:
                    water -= latte_water
                    milk -= latte_milk
                    coffee -= latte_coffee
                    cost = latte_price

    # Cappuccino
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

    if response == "cappuccino":
        if cappuccino_water > water:
            print(f"Sorry there is not enough water.")
        elif cappuccino_water < water:
            if cappuccino_milk > milk:
                print(f"Sorry there is not enough milk.")
            elif cappuccino_milk < milk:
                if cappuccino_coffee > coffee:
                    print(f"Sorry there is not enough coffee.")
                elif cappuccino_coffee < coffee:
                    water -= cappuccino_water
                    milk -= cappuccino_milk
                    coffee -= cappuccino_coffee
                    cost = cappuccino_price


        

    print(f"Water {water}, Milk {milk}, Coffee {coffee}")



    # 5. Process coins.
    # Ask how much coins you want to insert
    print(f"Please insert coins.")
    ask_quarter = int(input(f"how many quarters?: "))
    ask_dime = int(input(f"how many dimes?: "))
    ask_nickel = int(input(f"how many nickels?: "))
    ask_penny = int(input(f"how many pennies?: "))

    # Coin conversion
    quarter_total = .25 * ask_quarter
    dime_total = .10 * ask_dime
    nickel_total = .05 * ask_nickel
    penny_total = .01 * ask_penny

    # Get the total amount of coins inserted
    money_inserted = quarter_total + dime_total + nickel_total + penny_total
    # If there is money inserted in the machine, the amount will show up when "report" is typed
    if money_inserted > 0:
        money_inside = True



    # 6.  Check transaction successful?
    if cost > money_inserted:
        print("Sorry that's not enough money. Money refunded.")
        machine_off = True
    # If user overpays, user will get a refund
    elif cost < money_inserted:
        user_change = money_inserted - cost
        print(f"Here is ${user_change:.2f} dollars in change.")


    # 7. Make Coffee.
    print(f"Here is your {response} ☕. Enjoy!")



