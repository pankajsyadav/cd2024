# Purpose of the program: To calculate cost of fibre installation based on length of fiber required
# DSC510 - 3.1
# Week 3
# Programming Assignment Week 3
# Author Pankaj Yadav
# 06/23/2024


# Change Control Log:

# Change #:1
# Changes Made : Updated the if-else statement to include only the costing
#                Tried to make use of TRY-EXCEPTION statement to handle error
# Date of changes : 6/23/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 6/23/2024


# Prompt the welcome message
print("Welcome to the Neighbourhood Fiber Installation Inc.")
print("This Page provides total cost of installing a fiber.")

# Ask basic information required to create a costing sheet
user_name = input("Please provide your name: ")
company_name = input("Please provide the company name: ")
fiber_length = input("Please provide the length of fiber required (in foot): ")
cost_per_foot = 0.87  # The default cost per foot of fiber

print(" ")
print(f"Thank you {user_name} for providing all the required information.")
print("Please wait while we are generating your receipt.")

# Check if the value entered is float
try:  # Using the simple "try / except" to make sure the values entered are correct values.
    fiber_length = float(fiber_length)

except ValueError:  # exception description for user
    print("""                 
          !!!  PROGRAM STOPPED PROCESSING DUE TO AN EXCEPTION  !!!!
          Please provide the length of fiber in numeric format only.
            """)

# Performing calculations based on user input and decide the price to be charged based on the length of fiber
if fiber_length <= 100:  # No bulk discount upto 100 ft
    cost_per_foot = 0.87  # $0.87 is the cost of fiber installation per foot

elif 100 < fiber_length <= 250:  # Bulk discount @ $ 0.07 per foot
    cost_per_foot = 0.80  # $0.80 is the cost of fiber installation per foot

elif 250 < fiber_length <= 500:  # Bulk discount @ $ 0.17 per foot
    cost_per_foot = 0.70  # $0.70 is the cost of fiber installation per foot

elif fiber_length > 500:  # Bulk discount @ $ 0.37 per foot
    cost_per_foot = 0.50  # $0.50 is the cost of fiber installation per foot

# Lets calculate all required charges
total_cost = float(fiber_length
                   * cost_per_foot)  # total cost based on the fiber length after any discounts
labor_charge = float(total_cost
                     * 0.02)  # A 2% labor charge is levied on total cost
cost_to_tax = float(total_cost
                    + labor_charge)  # Total cost to tax
total_taxes = float(cost_to_tax
                    * 0.08)  # A tax of 8% is applied on total cost
final_cost = float(total_cost
                   + total_taxes
                   + labor_charge)  # Final balance the user will pay

# Creating a formatted receipt for user

print(f"""
--------------------------------------------------------------------
                  Fiber installation Receipt                        
--------------------------------------------------------------------
    Company Name                          : {company_name}      
    Total fiber to be installed (in foot) : {fiber_length}     
    Current installation cost per footage : $ 0.87  
    Bulk discount on purchase (per foot)  : $ {0.87 - cost_per_foot:.2f}          
    Installation charge                   : $ {total_cost:.2f}
    labor charge                          : $ {labor_charge:.2f}
    Tax @8%                               : $ {total_taxes:.2f} 
___________________________________________________________________
 Total cost of installation               : $ {final_cost:.2f}  
___________________________________________________________________
""")
