# Purpose of the program: To calculate cost of fibre installation based on length of fiber required using function
# DSC510 - 4.1
# Week 4
# Programming Assignment Week 4
# Author Pankaj Yadav
# 06/29/2024


# Change Control Log:

# Change #:1
# Changes Made : Created functions to
#                1. Check if a variable is not empty
#                2. Check if numeric variable is not zero or other type than float/ numeric
#                3. Calculations and costing sheet creation
#                4. Call to main function
# Date of changes : 6/29/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 6/30/2024


# Bring in Values as inputs

def var_check(varname):
    """This Function check if a variable is not intentionally left blank"""
    if len(varname) == 0:
        return var_check(input("This field can not be empty, please provide the requested information: "))
    else:
        return varname


def chk_float(invar):
    """This Function checks if the value  entered is a float or not
       Also checks if the entered value is greater than 0"""

    try:  # Using the simple "try / except" to make sure the values entered are correct values.
        if float(invar) == 0:
            return chk_float(input("Length can not be 0 or blank, please provide the requested information: "))
        else:
            return invar

    except ValueError:  # exception description for user
        return chk_float(input("Please re-enter the fibre length in numeric format only: "))


def costing_by_foot(fiber_len):
    """This function determines the cost per feet to be charged based on the length of fiber provided"""
    if fiber_len <= 100:
        return 0.87
    elif 100 < fiber_len <= 250:
        return 0.80
    elif 250 < fiber_len <= 500:
        return 0.70
    elif fiber_len > 500:
        return 0.50


def create_receipt(feet, cost):
    """
    This is the final function which brings in the cost and length after all checks and
    creates the final receipt for the end user
    """
    total_cost = float(feet
                       * cost)  # total cost based on the fiber length after any discounts
    labor_charge = float(total_cost
                         * 0.02)  # A 2% labor charge is levied on total cost
    cost_to_tax = float(total_cost
                        + labor_charge)  # Total cost to tax
    total_taxes = float(cost_to_tax
                        * 0.08)  # A tax of 8% is applied on total cost
    final_cost = float(total_cost
                       + total_taxes
                       + labor_charge)  # Final balance the user will pay

    print(" ")
    print(f"Thank you {user_name} for providing all the required information.")
    print("Please wait while we are generating your receipt.")

    print(f"""
        --------------------------------------------------------------------
                          Fiber installation Receipt                        
        --------------------------------------------------------------------
            Company Name                          : {company_name}      
            Total fiber to be installed (in foot) : {fiber_length}     
            Current installation cost per footage : $ 0.87  
            Bulk discount on purchase (per foot)  : $ {0.87 - cost:.2f}          
            Installation charge                   : $ {total_cost:.2f}
            labor charge                          : $ {labor_charge:.2f}
            Tax @8%                               : $ {total_taxes:.2f} 
        ___________________________________________________________________
         Total cost of installation               : $ {final_cost:.2f}  
        ___________________________________________________________________
        """)


# Defining the call to main

if __name__ == "__main__":

    # Prompt the welcome message
    print("Welcome to the Neighbourhood Fiber Installation Inc.")
    print("This Page provides total cost of installing a fiber.")

    # Ask basic information required to create a costing sheet
    user_name: str = var_check(input("Please provide your name: "))
    company_name = var_check(input("Please provide the company name: "))
    fiber_length = float(chk_float(var_check(input("Please provide the length of fiber required (in foot): "))))
    cost_per_foot = 0.87  # The default cost per foot of fiber

    # Creates the final receipt for the user
    create_receipt(fiber_length, costing_by_foot(float(fiber_length)))
