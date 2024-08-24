


# This code was designed to be ran through the command line in a terminal enviorment

import os, sys

windows_is_the_OS = False # This variable is set by the main programmer to ensure that terminal commands are correctly executed in clear_screen() and cancel_order()

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

current_order = [] # Customers order list. Created globally to be accessed from multiple functions
menu_items = {} # GLOBAL Create a dictionary to store the menu for later retrieval; THIS WILL BE A DICTIONARY WITH KEY = MENU ITEM NUMBER, AND VALUE = SUB-CATAGORY 
menu_category = None



def clear_screen(): # This function is used to clear the terminal screen based on if the program is running on windows, or a Mac / Linux system.
    if windows_is_the_OS:
        os.system('cls')
    else:
        os.system('clear')



def cancel_order():
    clear_screen()
    print("")
    print("We're sorry to see you go\n    and hope that you come back soon!\n")
    if windows_is_the_OS:
        os.system('cd')
        os.system('dir')
    else:
        os.system('pwd')
        os.system('ls')
    print("")
    sys.exit()



def main_menu():
    global current_order # Allow access to a global variable
    cancel_order_number = None
    # GLOBAL Create a dictionary to store the menu for later retrieval; THIS WILL BE A DICTIONARY WITH KEY = MENU ITEM NUMBER, AND VALUE = SUB-CATAGORY 
    global menu_items
    global menu_category

    clear_screen() # Clear terminal for a smooth look
    print("\nWelcome to THE GIGA-CHAD FOOD TRUCK!!!\nWe hope that you're having a great day, so that we can make it even better!!!\n") # Launch the store and present a greeting to the customer
    # 1. Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered

    # Customers may want to order multiple items, so let's create a continuous
    # loop
    placing_order = True # Changed variable name for clairity of purpose
    while placing_order:
        # Ask the customer from which menu category they want to order
        print("Hey look it's our main menu!")

        # Create a variable for the menu item number
        i = 1
        # Print the options to choose from menu headings (all the first level
        # dictionary items in menu).
        for key in menu.keys():
            print(f"{i}: {key}")
            # Store the menu category associated with its menu item number
            menu_items[i] = key # This line makes a new dictionary enterance in menu_items with the number i as the key, and "key" as the value
            # Add 1 to the menu item number
            i += 1

        # Get the customer's input
        cancel_order_number = len(menu) + 1
        menu_category = input(f"\nPlease enter a number listed above to see what we got!\nEnter {cancel_order_number} to cancel your order: ") # Needs to be an int = to the int key names in 

        # Check if the customer's input is a number
        if menu_category.isdigit() and (int(menu_category) in menu_items.keys() or int(menu_category) == cancel_order_number):
            menu_category = int(menu_category)
            if int(menu_category) in menu_items.keys():
                sub_menu()
            elif int(menu_category) == cancel_order_number:
                cancel_order()
        else:
            # Tell the customer they didn't select a number
            print(f"\n{menu_category} is not a menu option you silly goose!!!\n")

        while True:
            # Ask the customer if they would like to order anything else
            keep_ordering = input("Would you like to keep ordering? Please enter 'y' to continue or 'n' to cancel: ")

            # 5. Check the customer's input
            if keep_ordering.lower() == 'y':
                main_menu()
            elif keep_ordering.lower() == 'n':
                cancel_order()
            else:
            	print(f"\n{keep_ordering} is not a valid input you silly goose!!!\n")
                    # Keep ordering

                    # Exit the keep ordering question loop

                    # Complete the order

                    # Since the customer decided to stop ordering, thank them for
                    # their order

                    # Exit the keep ordering question loop


                    # Tell the customer to try again


    ''' # Print order function
    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Uncomment the following line to check the structure of the order
    #print(order)

    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")

    # 6. Loop through the items in the customer's order

        # 7. Store the dictionary items as variables


        # 8. Calculate the number of spaces for formatted printing


        # 9. Create space strings


        # 10. Print the item name, price, and quantity


    # 11. Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()
    # and print the prices.
   '''



def sub_menu():
    global menu_items
    global menu_category
    clear_screen()
    chillin_in_the_sub_menu_function = True
    # Save the menu category name to a variable
    menu_category_name = menu_items[int(menu_category)]
    print(f"\nWhich {menu_category_name} items would you like to order?\n")
    i = 1
    menu_items = {}
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    for key, value in menu[menu_category_name].items():
        # Check if the menu item is a dictionary to handle differently
        if type(value) is dict:
            for key2, value2 in value.items():
                num_item_spaces = 24 - len(key + key2) - 3
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                menu_items[i] = {
                    "Item name": key + " - " + key2,
                    "Price": value2
                }
                i += 1
        else:
            num_item_spaces = 24 - len(key)
            item_spaces = " " * num_item_spaces
            print(f"{i}      | {key}{item_spaces} | ${value}")
            menu_items[i] = {
                "Item name": key,
                "Price": value
            }
            i += 1

    print("\nEnter "+str(i)+" to go back to the main menu.")

    # 2. Ask customer to input menu item number
    while True:
        user_input = input("\nPlease enter a number that coresponds with the item you want!\nThen we will ask how many in the next question. ")
        if user_input.isdigit():
            user_input = int(user_input)

            print("TEMP LENGTH menu_items: ", len(menu_items))

            if user_input in range(1, len(menu_items) + 1):
                while True:
                    quantity_input = input('\nHow many "'+menu_items[user_input]['Item name']+'s" would you like? ')
                    if quantity_input.isdigit():
                        print(str(quantity_input)+" "+menu_items[user_input]["Item name"]+"s would cost X.")
                    else:
                    	print(f"\n{quantity_input} is not an input option you silly goose!!!")
            elif user_input == i:
            	main_menu()
            else:
                print(f"{user_input} is not an input option you silly goose!!!")
        else:
            print(f"{user_input} is not an input option you silly goose!!!")



    # 3. Check if the customer typed a number

        # Convert the menu selection to an integer


        # 4. Check if the menu selection is in the menu items

            # Store the item name as a variable


            # Ask the customer for the quantity of the menu item


            # Check if the quantity is a number, default to 1 if not


            # Add the item name, price, and quantity to the order list


            # Tell the customer that their input isn't valid


        # Tell the customer they didn't select a menu option



main_menu() # Execute the main_menu() first thing when running program


