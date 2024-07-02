# Purpose of the program: To calculate cost of fibre installation
# DSC510 - 2.1
# Week 2
# Programming Assignment Week 2
# Author Pankaj Yadav
# 06/13/2024


# Change Control Log:

# Change #:1
# Changes Made : Updated the print costing sheet code to use single print function
#                Corrected the spelling of fiber
# Date of changes : 6/13/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 6/13/2024

# Change #:2
# Changes Made : Updated code for few grammatical mistakes. Updated format per PEP8 standards
# Date of changes : 6/15/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 6/15/2024

# Prompt the welcome message
print("Welcome to the Neighbourhood Fiber Installation Inc.")
print("This Page provides total cost of installing a fiber.")

# Ask basic information required to create a costing sheet
user_name = input("Please provide your name: ")
company_name = input("Please provide the company name: ")
fiber_length = float(input("Please provide the length of fiber required (in foot): "))

print("")
print(f"Thank you {user_name} for providing all the required information.")
print("We are generating your receipt.")
# Performing calculations based on user input
total_cost = float(fiber_length
                   * 0.87)   # $0.87 is the cost of fiber installation per foot
labor_charge = float(total_cost
                     * 0.02)   # A 2% labor charge is levied on total cost
cost_to_tax = float(total_cost
               + labor_charge)  # Total cost to tax
total_taxes = float(cost_to_tax
                    * 0.08)    # A tax of 8% is applied on total cost
final_cost = float(total_cost
              + total_taxes
              + labor_charge) # Final balance the user will pay

# Creating a formatted receipt for user
print(f"""
--------------------------------------------------------------------
                  Fiber installation Receipt                        
--------------------------------------------------------------------
    Company Name                          : {company_name}      
    Total fiber to be installed (in foot) : {fiber_length}     
    Current installation cost per footage : $ 0.87             
    Installation charge                   : $ {total_cost:.2f}
    labor charge                          : $ {labor_charge:.2f}
    Tax @8%                               : $ {total_taxes:.2f} 
___________________________________________________________________
 Total cost of installation               : $ {final_cost:.2f}  
___________________________________________________________________
""")
