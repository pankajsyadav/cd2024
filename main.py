# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_inputs():
    temp = None
    temp_list = []
    # while temp != 'END':
    while True:
        temp = input("Please enter the temperature or 'END' to quit: ")
        if temp.isdigit():
            temp_list.append(int(temp))
        elif temp.upper() == 'END':
            out_var = ''' 
                     The Highest temperature is : {}
                     The Lowest temperature is : {}
                     The total observations provided : {}
                   '''.format(max(temp_list), min(temp_list), len(temp_list))
            return out_var


def main():
    print(get_inputs())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
