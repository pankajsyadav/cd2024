# Purpose of the program: This program creates a cash register program which provide final total
#                         in local currency and total number of items in cart
# DSC510 - 10.2
# Week 10
# Programming Assignment Week 10
# Author Pankaj Yadav
# 08/06/2024


# Change Control Log:

# Change #:1
# Changes Made : 1. import locale class and set itCreated empty dictionary
#                2. Created class cash register and initiate, define class setters and getters
#                3. define main and call to main
#                4. print outputs using locale call to currency symbol
# Date of changes : 08/06/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 08/06/2024


import locale

# Set the locale for currency formatting
locale.setlocale(locale.LC_ALL, locale.getlocale())


class Cash_Register:
    """ Define the class with the name cash register per assignment instructions."""

    def __init__(self):

        # Initialize the price and count within the class
        self.tot_amount = 0.0
        self.tot_count = 0


    def add_item(self, price):
        """ Add an item to the cash register."""

        self.tot_amount += price # The price parameter
        self.tot_count += 1  # The counter will keep adding item each time a prince is added

    def get_total(self):

        return 'Your total amount is : {}'.format(self.tot_amount)

    def get_count(self):
        return 'The total items in the cart : {}'.format(self.tot_count)

    def get_tot(self):  # remove this later if issue resolves
         return self.tot_amount

def main():
    print("\n\nWelcome to the Shop!\n")
    items = Cash_Register()

    while True:
        get_price = input("Enter the items price or Respond 'Done' to finish: ").upper()
        if get_price == 'D' or get_price == 'DONE' or get_price == 'DON':
            break
        try:
            price = float(get_price)
            items.add_item(price)
        except ValueError:
            print("Invalid input. Please enter a valid price.")

    print("\n\nThank you for Shopping with us!")

    print(f"\n{items.get_count()}")
    print(f"Total amount: {locale.currency(items.get_tot(), symbol=True)}")


if __name__ == "__main__":
    main()
