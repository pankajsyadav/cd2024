# This program fetches chucknorris jokes using request library
import os
import requests


# Define function for bulk ingest
def input_check():
    """ This function ask user to enter the number of jokes he would like to write in a go """

    n_jokes = input("Enter the number of jokes you would like to fetch from Norris: ")

    # Making sure the values provided are numeric
    try:
        n_jokes = int(n_jokes)
        return n_jokes

    # Ask to repeat if values are non integer
    except ValueError:
        print("Value entered is not a valid integer.")
        input_check()
        return n_jokes


# Create function to check if the file exists
def check_file_exists(file_path):
    """ function will make sure if file already exists and give user an option to write on same
        file or create a new one"""

    if os.path.exists(file_path):  # check if file exists

        # Ask the user to enter the response in case the user is willing to overwrite existing file
        file_exits_flag = input("Filename already exists, Do you want to overwrite it?:")

        if file_exits_flag.upper() == "YES":  # user is OK to overwrite existing file call print to file function
            return file_path

        elif file_exits_flag.upper() == "NO":  # user is NOT OK to overwrite existing file call filename function
            file_path = filename_function()
            return file_path
        else:
            return file_path

    else:
        return file_path


# define a function to ask user to provide a file name that he want to write the output to
def filename_function():
    # Ask user to provide the name of the file
    out_file_name = input('Enter output file name: ')

    # call function to make sure if file already exists
    check_file_exists(out_file_name)
    return out_file_name


def get_jokes():
    """ function uses requests library to get jokes from Norris api"""

    dict()
    r = requests.get('https://api.chucknorris.io/jokes/random')
    jsn = r.json()
    return jsn


def Write_file(file_name):
    """ This function writes out the jokes you would like to write in a go to a file"""

    with open(file_name, 'w') as f:

        # While the user still willing to keep reading jokes
        while True:

            # call get_jokes function to use API
            data = get_jokes()

            # Write the output to the file
            f.write(data['value'] + '\n')

            # Printing the joke to the output
            print(f'\nJoke : {data['value']} \n')

            # Asking user input if user wants to exit
            jokes = input('If you want to exist respond "Yes" else "No":')

            # if user wants to exit then break the loop else continue
            if jokes.upper() != 'YES' or jokes.upper() != 'Y':
                print('\nThank you for using this program. Hope you had some fun!')
                break

            else:
                continue


def pretty_print():
    """ This function will create an output which is indented and printed """

    while True:

        # Call to API function
        data = get_jokes()

        # Just print the joke
        print(f'\nJoke : {data['value']} \n')

        # If user wants to continue
        jokes = input('If you want to Continue? Respond "Yes" else "No":')

        # if user wants to exit then break the loop else continue
        if jokes.upper() == 'NO' or jokes.upper() == 'N':
            print('\nThank you for using this program. Hope you had some fun!')
            break
        else:
            continue


def main():
    """ Define main function for the program """

    # Welcome message
    print("\n Welcome To The Norris Joke Centre! \n\n")

    # Asking user input
    ready_for_jokes = input("Are you ready for some Norris jokes? (YES/NO): ")

    # If ready then continue else exit
    if ready_for_jokes.upper() == 'YES' or ready_for_jokes.upper() == 'Y':
        print("\nYAY! Lets have some fun\n")

        # Ask if user wants to save jokes in a text file as well
        get_choice = input("Would you like to save the jokes in a text file as well? (YES/NO): ")
        print('\n')

        # If user wants to save jokes
        if get_choice.upper() == "YES" or get_choice.upper() == "Y":

            # Ask user to enter a file name and do sanity checks
            use_filename = filename_function()

            Write_file(use_filename)

        # If user don't want to save jokes, just print to output window
        elif get_choice.upper() == "NO" or get_choice.upper() == "N":
            pretty_print()

    else:
        print("\nWe are sorry to let you go this soon! Lets meet again!\n")


if __name__ == '__main__':
    main()
