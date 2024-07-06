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

# Define the function to perform calculations
def performCalculation(operation):
    # Ask user to provide the numbers for operations
    num_input_1 = float(input('Enter the first number to perform the operation: '))
    num_input_2 = float(input('Enter the second number to perform the operation: '))

    # If user chose addition,
    if operation == 'a' or operation == 'A':
        print("Operation Performed: Addition")
        return (num_input_1
                + num_input_2)

    # If the user chose subtraction
    if operation == 's' or operation == 'S':
        print("Operation Performed: Subtraction")
        return (num_input_1
                - num_input_2)

    # If user wants to multiply the numbers
    if operation == 'm' or operation == 'M':
        print("Operation Performed: Multiplication")
        return (num_input_1
                * num_input_2)

    #  If user chose to divide the two numbers
    if operation == 'x' or operation == 'X':

        try:
            print("Operation Performed: Division")
            return (num_input_1
                    / num_input_2)

        # To handle the exception if user enters a zero value divisor
        except ZeroDivisionError:
            print("Division by zero not available")
            return performCalculation(operation)

    # find the modulo or remainder of the division
    if operation == 'y' or operation == 'Y':
        print("You have chose remainder")
        return (num_input_1
                % num_input_2)


# Define function to calculate the average of numbers
def calculateAverage():
    # As user to enter the list of numbers he wants to check the average of separated by spaces
    # in_list = list(map(int, input('Enter the numbers separated by spaces: ').split()))

    # Calculate and print the average eof numbers
    # print("The average is: ", sum(in_list) / len(in_list))

    # Calculate the sum & average using for loop
    # Ask the user to enter the iterations they want to use to enter the number
    iter_var = int(input('Enter how many numbers you would like to calculate the average for: '))
    total = 0

    # initiate the for loop to ask user to provide the number and iterate the loop using inter_var
    for num in range(iter_var):
        total += int(input(f'Enter the number {num+1}: '))

    # The Print the total sum
    print(f'Sum Total: {total}')

    # Calculate average based on total sum and numbers
    print(f"The average of the above {iter_var} numbers is: ", total / iter_var)


if __name__ == "__main__":
    while True:
        in_val = input(
            "What would you like to do? Enter 'A' for averages, 'C' for Arithmetic operations and 'Q' to quit the "
            "application:")
        if in_val == 'q' or in_val == 'Q':
            break
        elif in_val == 'c' or in_val == 'C':
            op_value = input("Please provide the operation you want to perform: "
                             "A for Addition, S for Subtraction, M for Multiplication, X for Division, "
                             "Y for Remainder : ")
            print(f"The answer is {performCalculation(op_value)}")

        elif in_val == 'a' or in_val == 'A':
            calculateAverage()

        else:
            print('Please provide the correct option as stated below')