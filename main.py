from menu import MENU, resources

# Flag to indicate that coffee machine is off or on
machine_off = False

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# response = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
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
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g")

# If you type "report" as response, it will print the resource values
# if response == "report":
#     print_report(resources)


# 4. Check resources sufficient?

# 5. Process coins.

# 6.  Check transaction successful?

# 7. Make Coffee.



