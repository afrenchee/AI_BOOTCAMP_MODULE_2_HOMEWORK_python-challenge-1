


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
	"Desserts": {
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
final_order_cost = 0
menu_items = {} # GLOBAL Create a dictionary to store the menu for later retrieval; THIS WILL BE A DICTIONARY WITH KEY = MENU ITEM NUMBER, AND VALUE = SUB-CATAGORY 
menu_category = None

truck_name = "THE GIGA_CHAD FOOD TRUCK"



def clear_screen(): # This function is used to clear the terminal screen based on if the program is running on windows, or a Mac / Linux system.
	if windows_is_the_OS:
		os.system('cls')
	else:
		os.system('clear')



def end_program():
	if windows_is_the_OS:
		os.system('cd')
		os.system('dir')
	else:
		os.system('pwd')
		os.system('ls')
	print("")
	sys.exit()



def cancel_order():
	clear_screen()
	print("\nWe're sorry to see you go\n    and hope that you come back soon!\n")
	end_program()



def print_invalid_input(invalid_input):
	print(f"\n{invalid_input} is not an input option you silly goose!!!\n")



def main_menu():
	global current_order # Allow access to a global variable
	cancel_order_number = None
	# GLOBAL Create a dictionary to store the menu for later retrieval; THIS WILL BE A DICTIONARY WITH KEY = MENU ITEM NUMBER, AND VALUE = SUB-CATAGORY 
	global menu_items
	global menu_category

	clear_screen() # Clear terminal for a smooth look
	print("\nWelcome to "+truck_name+"!!!\n    We hope that you're having a great day, so that we can make it even better!!!\n") # Launch the store and present a greeting to the customer
	
	placing_order = True # Changed variable name for clairity of purpose
	while placing_order:
		print("Hey look it's our main menu!")

		i = 1
		for key in menu.keys():
			print(f"{i}: {key}")
			menu_items[i] = key # This line makes a new dictionary enterance in menu_items with the number i as the key, and "key" as the value
			i += 1

		if len(current_order) > 0:
			cancel_order_number = len(menu) + 2
			print(f'\nEnter "{i}" to view, edit, or checkout your current order!')
		else:
			cancel_order_number = len(menu) + 1
		menu_category = input(f"\nPlease enter a number listed above to see what we got!\nEnter {cancel_order_number} to cancel your order: ") # Needs to be an int = to the int key names in 

		if menu_category.isdigit() and (int(menu_category) in menu_items.keys() or int(menu_category) == cancel_order_number or (int(menu_category) == i and len(current_order) > 0)):
			menu_category = int(menu_category)
			if int(menu_category) in menu_items.keys():
				sub_menu()
			elif int(menu_category) == cancel_order_number:
				cancel_order()
			elif int(menu_category) == i and len(current_order) > 0:
				view_edit_and_finish_order()
		else:
			print_invalid_input(menu_category)

		while True:
			keep_ordering = input("Would you like to keep ordering? Please enter 'y' to continue or 'n' to cancel: ")

			if keep_ordering.lower() == 'y':
				main_menu()
			elif keep_ordering.lower() == 'n':
				cancel_order()
			else:
				print_invalid_input(keep_ordering)



def sub_menu():
	global current_order
	global menu_items
	global menu_category
	clear_screen()

	menu_category_name = menu_items[menu_category]

	print(f"\nWhich {menu_category_name} items would you like to order?\n")
	i = 1
	sub_menu_items = {}  # Use a separate dictionary for the sub-menu items
	print("Item # | Item name                | Price")
	print("-------|--------------------------|-------")

	for key, value in menu[menu_category_name].items():
		if isinstance(value, dict):
			for key2, value2 in value.items():
				num_item_spaces = 24 - len(key + key2) - 3
				item_spaces = " " * num_item_spaces
				print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
				sub_menu_items[i] = {
					"Item name": key + " - " + key2,
					"Price": value2
				}
				i += 1
		else:
			num_item_spaces = 24 - len(key)
			item_spaces = " " * num_item_spaces
			print(f"{i}      | {key}{item_spaces} | ${value}")
			sub_menu_items[i] = {
				"Item name": key,
				"Price": value
			}
			i += 1

	print(f"\nEnter {i} to go back to the main menu.\n")

	while True:
		user_input = input("Please enter a number that corresponds with the item you want: ")
		# print("")
		if user_input.isdigit():
			user_input = int(user_input)
			if user_input in sub_menu_items:
				while True:
					quantity_input = input(f'You picked "{sub_menu_items[user_input]["Item name"]}"! How many would you like?\nEnter 0 to go back. ')
					if quantity_input.isdigit() or quantity_input == "":
						if quantity_input == "": # Default quantity to 1 if no input
							quantity_input = 1
						
						quantity_input = int(quantity_input)
						if quantity_input == 0:
							sub_menu()						
						else:
							total_cost = round(sub_menu_items[user_input]["Price"] * quantity_input, 2)
							print(f'\n{quantity_input} "{sub_menu_items[user_input]["Item name"]}" would cost ${total_cost}.\n')

							while True:
								confirmation = input(f'Just to double check, you want to add {quantity_input} "{sub_menu_items[user_input]["Item name"]}" to your order for ${total_cost}?\nEnter "y" to add or "n" to go back. ')
								if confirmation.lower() == 'y':
									new_item = {
										"Item Name": sub_menu_items[user_input]["Item name"],
										"Quantity": quantity_input,
										"Individual Price": sub_menu_items[user_input]["Price"],
										"Total Price": total_cost
										# Add string to print
									}
									current_order.append(new_item)

									clear_screen()
									print(f'\n{current_order[len(current_order) - 1]["Quantity"]} "{current_order[len(current_order) - 1]["Item Name"]}" were added to you order, adding ${current_order[len(current_order) - 1]["Total Price"]} to your total price!')
									print(
										f'\nEnter "1" to view, edit, or checkout your current order!\n'
										f'Enter "2" to add more {menu_category_name}!\n'
										'Enter "3" to return to the main menu!\n'
										'Enter "4" to cancel the order!\n'
									)
									while True:
										view_order_question = input("Please enter a number listed above to proceed: ")
										if view_order_question.isdigit() and int(view_order_question) > 0 and int(view_order_question) <= 4:
											view_order_question = int(view_order_question)
											if view_order_question == 1:
												view_edit_and_finish_order()
											elif view_order_question == 2:
												sub_menu()
											elif view_order_question == 3:
												main_menu()
											elif view_order_question == 4:
												cancel_order()
										else:
											print_invalid_input(view_order_question)
								elif confirmation.lower() == 'n':
									sub_menu()
								else:
									print_invalid_input(confirmation)
					else:
						print_invalid_input(quantity_input)
			elif user_input == i:
				main_menu()
			else:
				print_invalid_input(user_input)
		else:
			print_invalid_input(user_input)



def view_edit_and_finish_order():
	global current_order
	global final_order_cost
	clear_screen()
	display_order()

	while True:
		#Ask to either edit, or finish order.
		print(
			'\nEnter "1" to cash out and purchase your order!\n'
			'Enter "2" to edit your order!\n'
			'Enter "3" to return to the main menu: \n'
		)
		while True:
			finish_order_input = input("Please enter one of the numbers listed above to proceed: ")
			if finish_order_input.isdigit() and int(finish_order_input) > 0 and int(finish_order_input) <= 3:
				finish_order_input = int(finish_order_input)
				if finish_order_input == 1:
					finish_order()
				elif finish_order_input == 2:
					edit_order()
				if finish_order_input == 3:
					main_menu()
			else:
				print_invalid_input(finish_order_input)



def display_order():
	global current_order
	global final_order_cost
	final_order_cost = 0
	if len(current_order) > 0:
		print("\nYour current order contains:") # Print out order in the recipt format the assignment wants
		i = 0
		for obj in current_order:
			i += 1
			print(str(i)+'. "'+str(obj["Item Name"])+'": Your order contains '+str(obj["Quantity"])+' of these at $'+str(obj["Individual Price"])+' each, adding $'+str(obj["Total Price"])+' to your order!')
			final_order_cost = round(final_order_cost + float(obj["Total Price"]), 2)

		print("\nYour orders total cost is $"+str(final_order_cost)+"\n")
	else:
		print("\nYour current order does not contain any items!") # Print out order in the recipt format the assignment wants



def edit_order():
	global current_order
	clear_screen()
	print("\nYou've selected that you want to edit your order!")
	display_order()
	while True:
		edit_selection = input('Enter the number displayed to the left of the item that you want to remove or change the quantity of,\nor enter "b" to go back! ')
		if edit_selection.isdigit() and int(edit_selection) > 0 and int(edit_selection) <= len(current_order):
			clear_screen()
			display_order()
			edit_selection = int(edit_selection)
			print(
				f'\nEnter "1" to remove all "{current_order[edit_selection - 1]["Item Name"]}" from your order!\n'
				f'Enter "2" to change the quantity of "{current_order[edit_selection - 1]["Item Name"]}" in your order!\n'
				'Enter "3" to go back.'
			)
			while True:
				edit_option = input("Please enter one of the options listed above: ")
				if edit_option.isdigit() and int(edit_option) >= 1 and int(edit_option) <= 3:
					edit_option = int(edit_option)

					if edit_option == 1:
						del current_order[edit_selection - 1]
						if len(current_order) == 0:
							main_menu()
						elif len(current_order) > 0:
							view_edit_and_finish_order()
					elif edit_option == 2:
						while True:
							new_quantity = input(f'Enter a new quantity for "{current_order[edit_selection - 1]["Item Name"]}": ')
							if new_quantity.isdigit() and int(new_quantity) >= 0:
								new_quantity = int(new_quantity)
								if new_quantity == 0:
									while True:
										confirm = input(f'\nUpdating the quantity of "{current_order[edit_selection - 1]["Item Name"]}" to {new_quantity} will remove the item from your order.\nEnter "y" to proceed or "n" to calcel changing the quantity: ')
										if confirm.lower() == 'y':
											del current_order[edit_selection - 1]
											view_edit_and_finish_order()
										elif confirm.lower() == 'n':
											view_edit_and_finish_order()
										else:
											print_invalid_input(confirm)
								else:
									new_price = round(float(current_order[edit_selection - 1]["Individual Price"]) * float(new_quantity), 2)
									while True:
										confirm = input(f'\nUpdating the quantity of "{current_order[edit_selection - 1]["Item Name"]}" to {new_quantity} will cost ${new_price}.\nEnter "y" to proceed or "n" to cancel changing the quantity: ')
										if confirm.lower() == 'y':
											current_order[edit_selection - 1]["Quantity"] = new_quantity
											current_order[edit_selection - 1]["Total Price"] = new_price
											view_edit_and_finish_order()
										elif confirm.lower() == 'n':
											view_edit_and_finish_order()
										else:
											print_invalid_input(confirm)
							else:
								print_invalid_input(new_quantity)
					elif edit_option == 3:
						view_edit_and_finish_order()
				else:
					print_invalid_input(edit_option)
		elif edit_selection.lower() == 'b':
			view_edit_and_finish_order()
		else:
			print_invalid_input(edit_selection)



def finish_order():
	clear_screen()
	display_order()
	print('Enter "y" to purchase this order and print the recipt!\nEnter "n" to go back!\nEnter "c" to cancel ordering\n')
	while True:
		finishing_input = input("Please enter one of the options listed above: ")
		if finishing_input.lower() == 'y':
			print_recipt()
		elif finishing_input.lower() == 'n':
			view_edit_and_finish_order()
		elif finishing_input.lower() == 'c':
			clear_screen()
			display_order()
			print("Canceling will delete your enitre order and end the program!")
			print('\nEnter "c" to cancel your order and end the program!\nEnter "b" to go back and view your order!')
			while True:
				cancel_input = input("Please enter one of the options listed above: ")
				if cancel_input.lower() == 'c':
					cancel_order()
				elif cancel_input.lower() == 'b':
					view_edit_and_finish_order()
				else:
					print_invalid_input(cancel_input)

		else:
			print_invalid_input(finishing_input)



def print_recipt():
	clear_screen()
	item_name_string_length = 26
	indv_price_string_length = 12
	quantity_string_length = 9
	total_item_price_string_length = 16
	print("\nThank you for visiting "+truck_name+"!!!\n    We hope that we've just made your day even better!!!\n")
	print("Item name                 | Indv. Price  | Quantity | Total Item Price |")
	print("--------------------------|--------------|----------|------------------|")
	for obj in current_order:
		item_name = str(obj["Item Name"])
		quantity = str(obj["Quantity"])
		indv_price = str(obj["Individual Price"])
		total_item_price = str(obj["Total Price"])

		item_name_additional_spaces_required = item_name_string_length - len(item_name)
		item_name_additional_spaces_string = " " * item_name_additional_spaces_required

		indv_price_additional_spaces_required = indv_price_string_length - len(indv_price)
		indv_price_additional_spaces_string = " " * indv_price_additional_spaces_required

		quantity_additional_spaces_required = quantity_string_length - len(quantity)
		quantity_additional_spaces_string = " " * quantity_additional_spaces_required

		total_item_price_additional_spaces_required = total_item_price_string_length - len(total_item_price)
		total_item_price_additional_spaces_string = " " * total_item_price_additional_spaces_required

		print(item_name + item_name_additional_spaces_string + "| $" + indv_price + indv_price_additional_spaces_string + "| " + quantity + quantity_additional_spaces_string + "| $" + total_item_price + total_item_price_additional_spaces_string + "|")
	print("")
	print(f"Your orders total cost was ${final_order_cost}") # calculated in display_order()
	print()
	end_program()



if __name__ == "__main__":
	main_menu() # Execute the main_menu() first thing when running program


