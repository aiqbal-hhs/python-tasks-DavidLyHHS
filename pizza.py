from collections import namedtuple

# Pizza to price
pizza_to_price = {'Classic Cheese': 5.00, 'Classic Veggie': 5.00, 'Pepperoni': 5.00, 'Beef & Onion': 5.00, 'Hawaiian': 5.00, 'Margherita': 8.50, 'Chicken Deluxe': 8.50, 'Meat Lovers': 8.50, 'Garlic Prawn': 8.50, 'Americano': 8.50, 'Supreme': 8.50, 'Italian': 8.50,}

# Index of pizza to price
index_to_price = {'1': 5.00, '2': 5.00, '3': 5.00, '4': 5.00, '5': 5.00, '6': 8.50, '7': 8.50, '8': 8.50, '9': 8.50, '10': 8.50, '11': 8.50, '12': 8.50,}

# Index to pizza
index_to_pizza = {'1': '- Classic Cheese', '2': '- Classic Veggie', '3': '- Pepperoni', '4': '- Beef & Onion', '5': '- Hawaiian', '6': '- Margherita', '7': '- Chicken Deluxe', '8': '- Meat Lovers', '9': '- Garlic Prawn', '10': '- Americano', '11': '- Supreme', '12': '- Italian'}

# Pizza Menu 
MenuEntry = namedtuple('MenuEntry', ['index','pizza','price'])
pizza_options = []
pizza_options.append(MenuEntry(1, 'Classic Cheese', '$5.00'))
pizza_options.append(MenuEntry(2, 'Classic Veggie', '$5.00'))
pizza_options.append(MenuEntry(3, 'Pepperoni', '$5.00'))
pizza_options.append(MenuEntry(4, 'Beef & Onion', '$5.00'))
pizza_options.append(MenuEntry(5, 'Hawaiian', '$5.00'))
pizza_options.append(MenuEntry(6, 'Margherita', '$8.50'))
pizza_options.append(MenuEntry(7, 'Chicken Deluxe', '$8.50'))
pizza_options.append(MenuEntry(8, 'Meat Lovers', '$8.50'))
pizza_options.append(MenuEntry(9, 'Garlic Prawn', '$8.50'))
pizza_options.append(MenuEntry(10, 'Americano', '$8.50'))
pizza_options.append(MenuEntry(11, 'Supreme', '$8.50'))
pizza_options.append(MenuEntry(12, 'Italian', '$8.50\n'))

# Toppings Menu
ToppingEntry = namedtuple('ToppingEntry', ['index','topping','price'])
topping_options = []
topping_options.append(ToppingEntry(1, 'Extra Cheese', '$0.50'))
topping_options.append(ToppingEntry(2, 'Extra Onion', '$0.50'))
topping_options.append(ToppingEntry(3, 'Extra Mushroom', '$0.50'))
topping_options.append(ToppingEntry(4, 'Extra Pepperoni', '$0.50'))
topping_options.append(ToppingEntry(5, 'Extra Olives', '$0.50'))
topping_options.append(ToppingEntry(6, 'Extra Ham', '$0.50'))

# Create an empty list to store the orders

order_list = []

topping = []
order_cost = 0

# Formats the pizza menu
def pizza_menu():
    for entry in pizza_options:
        index = str(getattr(entry,'index')).ljust(5)
        pizza = getattr(entry,'pizza').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{0}{1}{2}'.format(index,pizza,price))

# Formats the pizza menu
def topping_menu():
    for entry in topping_options:
        index = str(getattr(entry,'index')).ljust(5)
        topping = getattr(entry,'topping').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{0}{1}{2}'.format(index,topping,price))
    
# toppings to price list
index_to_topping = {'1': ' + Extra Cheese', '2': ' + Extra Onions', '3': ' + Extra Mushroom', '4': ' + Extra Pepperoni', '5': ' + Extra Olives', '6': ' + Extra Ham'}
# Contact information for delivery
contact = {}

name = input("What is your name? ").title()
contact['Name'] = name
print("\nWelcome, {} to Henderson Pizza Palace!\n".format(name))

# Menu function prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service.
def menu():
  """Prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service."""
  print("Type: \n",
          "'1' to view menu\n",
          "'2' to view pizza options and prices\n",
          "'3' to order pizza\n",
          "'4' to view order\n",
          "'5' to cancel ordering")

# Menu function prints out the instructions for the user so they can use a service option for the Henderson Pizza Palace service.
def service_menu(order_cost, topping):
  """Prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service."""
  print("How would you like the pizza to get to you? \n",
          "'1' Delivery ($3 surcharge)\n",
          "'2' Pick-up\n",
          "'3' to go back menu")
  service_repeat = True
  while service_repeat:
      service_option = input("\nPlease enter here: \n").strip()
      # Asks the user to input address and phone number
      # Will ask if contact information is correct
      # Will remove contact information and repeat if user inputs "no"
      if service_option == "1":
        print("You chose delivery")
        order_cost += 3
        contact_repeat = True
        while contact_repeat == True:
          try:
            phone_number = int(input("What is your phone number?"))
          except ValueError:
            print("Please input integer only...")
            continue
          contact['Phone number'] = phone_number
          address = input("What is your address?")
          contact['Address'] = address.title()
          print(contact)
          information = input("Is your contact information correct? (Answer: 'yes' or 'no'").strip().lower()
          if information == "no":
            print("Please resubmit your contact information")
            continue
          elif information == "yes":
            print("Thank you!")
            pizza_menu()
            topping_menu()
            contact_repeat = False
            break
          else:
            print("Please enter a valid response!")

        order(order_cost)
        service_repeat = False
            
      elif service_option == "2":
        print("You chose pick-up")
        pizza_menu()
        topping_menu()
        order(order_cost)
      elif service_option == "3":
        break
      else:
        print("Please choose a valid number")

# Function that takes in the users orders 
def order(order_cost):
  while True:
    new_order = input("Enter your order by entering the number next to the name of the pizza on the menu or type 'end' to finish order.\nYou can cancel your order at anytime by inputting 'cancel'")
    if new_order == "end":
        print("Contact Information = {}".format(contact))
        print("Your order is: ")
        view_order()
        correct = input("Is your order correct? Please input 'yes' or 'no'.").strip().lower()
        if correct == "yes":
            print("Your order will be ready soon! Thanks for ordering at Henderson Pizza Palace!")
            order_list.clear()
            break
        elif correct == "no":
            order_list.clear()
    elif new_order in index_to_pizza:
        order_list.append(index_to_pizza.get(new_order))
        if new_order == "1" or new_order == "2" or new_order == "3" or new_order == "4" or new_order == "5":
            order_cost += 5
            while True:
                topping = input("Enter any toppings you would like by entering the number next to the name of the topping on the menu or type 'end' to finish order")
                if topping in index_to_topping:
                    order_list.append(index_to_topping.get(topping))
                    order_cost += 0.5
                elif topping == "end":
                    print("Your total order cost is ${}".format(order_cost))
                    break
                elif topping == "cancel":
                    break
                else:
                    print("That is not one of the topping options!")
        elif new_order == "6" or new_order == "7" or new_order == "8" or new_order == "9" or new_order == "10" or new_order == "11" or new_order == "12":
            order_cost += 8.5
            while True:
                topping = input("Enter any toppings you would like by entering the number next to the name of the topping on the menu or type 'end' to finish order")
                if topping in index_to_topping:
                    order_list.append(index_to_topping.get(topping))
                    order_cost += 0.5
                elif topping == "end":
                    print("Your total order cost is ${}".format(order_cost))
                    break
                elif topping == "cancel":
                    break
                else:
                    print("That is not one of the topping options!")
    elif new_order == "cancel":
        order_list.clear()
        menu()
        break
    else:
        print("Sorry, that is not one of the pizza options")

# Function that shows current orders in the order_list
def view_order():
  if len(order_list) > 0:
    for order in order_list:
      print("{}".format(order, topping))
  else:
    print("You have no orders yet!")

# Print menu
menu()

# Run program loop
repeat = True
while repeat == True:

  # Ask user for input and
  option = input("\nWhat would you like to do? \n").strip()

  # Check input and run the chosen function
  if option == "1":
    menu()
  elif option == "2":
    pizza_menu()
    topping_menu()
  elif option == "3":
    service_menu(order_cost, topping)
  elif option == "4":
    view_order()
  elif option == "5":
    print("Goodbye {}, thanks for buying from Henderson Pizza Palace!".format(name))
    repeat = False
  else:
    print("That wasn't an option")
