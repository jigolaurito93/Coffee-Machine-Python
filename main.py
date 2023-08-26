from menu import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

money = 0

espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# Flag to indicate that coffee machine is off or on
machine_off = False

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
response = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
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


    

print(f"Water {water}, Milk {milk}, Coffee {coffee}")



# 5. Process coins.
print(f"Please insert coins.")
ask_quarter = int(input(f"how many quarters?: "))
ask_dime = int(input(f"how many dimes?: "))
ask_nickel = int(input(f"how many nickels?: "))
ask_penny = int(input(f"how many pennies?: "))

quarter_total = .25 * ask_quarter
dime_total = .10 * ask_dime
nickel_total = .05 * ask_nickel
penny_total = .01 * ask_penny

money_total = quarter_total + dime_total + nickel_total + penny_total





# 6.  Check transaction successful?

# 7. Make Coffee.



