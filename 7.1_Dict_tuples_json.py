# Purpose of the program: The program counts the number of words in a file and prints the total number of occurrences
#                         Program uses concept of dictionaries, strings, for loop and main function
# DSC510 - 7.1
# Week 7
# Programming Assignment Week 7
# Author Pankaj Yadav
# 07/21/2024


# Change Control Log:

# Change #:1
# Changes Made : 1. Created empty dictionary
#                2. Created functions main, add_word, process_line & pretty_print
#                3. Perform operation to provide number of word count
#                4. Call to main function
# Date of changes : 07/21/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 07/21/2024


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
    # Open the file in read mode
    gba_file = open('gettysburg.txt', 'r')

    # read each line using a for loop
    for line in gba_file:
        # Strip white spaces from the string
        lines_str = line.strip()

        # Call function process line to further process the string
        process_line(lines_str)

    # Use pretty print to print the final output
    pretty_print()


# Call to the main
if __name__ == '__main__':
    main()
