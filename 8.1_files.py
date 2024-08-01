# Purpose of the program: The program counts the number of words in a file and writes the total number of occurrences
#                         Program uses concept of dictionaries, strings, for loop and main function
# DSC510 - 8.1
# Week 8
# Programming Assignment Week 8
# Author Pankaj Yadav
# 07/28/2024


# Change Control Log:

# Change #:1
# Changes Made : 1. Created empty dictionary
#                2. Created functions main, add_word, process_line & pretty_print
#                3. Perform operation to provide number of word count
#                4. Call to main function
# Date of changes : 07/28/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 07/28/2024

import os


# Create function to check if the file exists
def check_file_exists(file_path):
    if os.path.exists(file_path):
        file_exits_flag = input("Filename already exists, Do you want to overwrite it?:")
        if file_exits_flag.upper() == "YES":  # user is OK to overwrite existing file call print to file function
            return file_path

        elif file_exits_flag.upper() == "NO":  # user is NOT OK to overwrite existing file call filename function
            file_path = filename_function()
            return file_path


# define a function to ask user to provide a file name that he want to write the output to
def filename_function():
    # Ask user to provide the name of the file
    out_file_name = input('Enter output file name: ')
    check_file_exists(out_file_name)
    return out_file_name


# process output file
def process_file(file_provided):
    print("Processing file...")

    # Open the file to write
    with open(file_provided, 'w') as file:
        # Sort the dictionary by max to min values
        sorted_dict = sorted(dict_word_list.items(), key=lambda x: x[1], reverse=True)

        file.write(f'Total Words in Dictionary :{len(sorted_dict)} \n')

        # Print Header
        file.write('\n    {l1:<12}   {l2:>10} \n ------------------------------ \n\n'.format(l1='WORDS', l2='COUNT'))

        # Print each key value pair
        for (key, value) in sorted_dict:
            file.write('    {key:<12}   {value:>10}\n'.format(key=key, value=value))

    # write to the file the values from inputs


# Get the name and info about file you want to read in
def in_file_name():
    # Ask user to enter the filename and check if the file exists. Read the data from the file if exists
    infile_name = input('Please enter the name of file you want to process: ')

    # Check if the file exists
    if os.path.exists(infile_name):
        return infile_name

    else:
        print('File does not exist, please try again.')
        infile_name = in_file_name()
        return infile_name


# Create empty dictionary. This dictionary is defined global to be referred across the functions
dict_word_list = dict()


# Create function add_word which will add new word to the list
def add_word(inlist):
    """ this function adds a word to the dictionary defined at the top """

    # If the word is not present in the dictionary then the word will be added as key
    # and the value is updated to 1

    if inlist not in dict_word_list:
        dict_word_list[inlist] = 1

    # If the word is present in that situation only the counter is incremented by 1
    else:
        dict_word_list[inlist] += 1


# Create a function to process each line from the text file and remove unwanted characters then call add word function
def process_line(line_str):
    """ This function processes a line of string provided and removes the punctuation characters present in it"""

    # remove punctuations as listed
    line_str = line_str.replace(',', '').replace('.', '').replace('-', '').replace('/n', '')

    # Make everything proper case
    line_str = line_str.title()

    # Create a string out of line
    split_list = line_str.split()

    # For each word in string, call add word function
    for word in split_list:
        add_word(word)


# Function to print the file properly
def pretty_print():
    """ This function will create an output which is indented and printed """

    # Sort the dictionary by max to min values
    sorted_dict = sorted(dict_word_list.items(), key=lambda x: x[1], reverse=True)

    print(f'''
    Total Words in Dictionary :{len(sorted_dict)}
    ''')

    # Print Header
    print('''
    WORD               COUNT
    -------------------------
    ''')

    # Print each key value pair
    for (key, value) in sorted_dict:
        print(f'    {key:<12}   {value:>8}')


# Define the main function
def main():
    # Get the name of file from user to be process and do some sanity checks
    file_name = in_file_name()
    print(file_name)

    # Open the file in read mode
    gba_file = open(file_name, 'r')

    # read each line using a for loop
    for line in gba_file:
        # Strip white spaces from the string
        lines_str = line.strip()

        # Call function process line to further process the string
        process_line(lines_str)

    # Now the file is read and processed. Let's ask user the name of file to write data to and do some checks
    get_file_name = filename_function()
    print(get_file_name)

    # Now lets process the information and write it to file calling process_file function
    process_file(get_file_name)

    # Use pretty print to print the final output
    pretty_print()


# Call to the main
if __name__ == '__main__':
    main()
