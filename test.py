# DSC 510
# Week 3
# Programming Assignment Week 2
# Purpose: Estimate cost of installing fiber optic cables
# Author: Jesse Caldo
# 6/23/2020

# Customer class to hold all values
class Customer:
    user = None
    company_name = None
    length = None

    # class initializer to initialize values
    def __init__(self, init_user, init_length, init_company_name):
        self.user = init_user
        self.length = init_length
        self.company_name = init_company_name
        self.validate()

    # validate if all fields are valid
    def validate(self):
        if self.user == "" or self.user is None:
            self.user = input("Missing user, Please enter username: ")
            while len(self.user) == 0:
                self.user = input("Missing user, Please enter username: ")

        if self.company_name == "" or self.company_name is None:
            self.company_name = input("Missing company name, Please enter "
                                      "company name: ")
            while len(self.company_name) == 0:
                self.company_name = input("Missing company name, Please enter "
                                          "company name: ")

        if self.length == 0:
            self.length = input("Length cannot be 0, Please enter length > "
                                "0: ")
            while self.length == 0:
                self.length = input(
                    "Length cannot be 0, Please enter length > "
                    "0: ")


# Parse input string to float
def parse(string):
    try:
        return float(string)
    except ValueError:
        return parse(input("Please enter number of feet to be installed: "))


# Generate receipt using company name and length that will be installed
# Change#:1
# Change(s) Made: Added discount based on length of installation
# Date of Change: 6/17/2024
# Author: Jesse Caldo
# Change Approved by: Jesse Caldo
# Date Moved to Production: 6/17/2024
def generate_receipt(customer_info):
    installation_cost = .87
    if customer_info.length > 500:
        installation_cost = .50
    elif customer_info.length > 250:
        installation_cost = .70
    elif customer_info.length > 100:
        installation_cost = .80
    total_cost = customer_info.length * installation_cost
    tax = total_cost * .10
    print(f"""+-----------------------------------+
+ Company Name : {customer_info.company_name:>16}   +
+ Length (ft): {customer_info.length:>18}   +
+ Installation Cost:      $.87/ft   +
+ Sub Total : {total_cost:>19}   +
+ Tax : {tax.__round__(2):>25}   +
+ Total : {(total_cost + tax).__round__(2):>23}   +
+-----------------------------------+""")


# Main function for program
if __name__ == "__main__":
    user = input("Hello, please enter username: ")
    company_name = input("Enter company name: ")
    length = parse(input("Enter Number of feet to be installed: "))
    customer = Customer(user, length, company_name)
    generate_receipt(customer)
