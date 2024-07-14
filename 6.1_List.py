# Purpose of the program: The program ask user to input a list of temperatures and based upon user input
#                         determine the number of temperatures in the program, determine the largest temperature,
#                         and the smallest temperature.
# DSC510 - 5.1
# Week 5
# Programming Assignment Week 5
# Author Pankaj Yadav
# 07/06/2024


# Change Control Log:

# Change #:1
# Changes Made : 1. Created function for calculations
#                2. Ask user to enter choices
#                3. Perform operation to provide max, min and count of observations
#                4. Call to main function
# Date of changes : 07/13/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 07/14/2024



def temp_calc():

    # General Message for user
    print('This program provides n, min and max of temperatures provided by user.')

    # Define initial variables
    temp_list = []

    # The While loop to exit when user want to quit.
    while True:

        # Ask user to input temperatures and exit condition
        temp = input("Please enter the temperature or 'END' to quit: ")

        # Making sure that entered value is number then append
        if temp.isdigit():
            temp_list.append(int(temp))

        # Else if the entered value is to quit then finish.
        elif temp.upper() == 'END':
            out_var = ''' 
            The total observations provided : {}
            The Highest temperature is : {}
            The Lowest temperature is : {} '''.format(len(temp_list), max(temp_list), min(temp_list))
            return out_var

def main():
    print(temp_calc())


if __name__ == '__main__':
    main()
