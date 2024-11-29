# Purpose of the program: This program creates a weather report based on the user inputs. It uses openweather api
#                         to provide the information
# DSC510 - 10.1
# Week 10
# Programming Assignment Week 10
# Author Pankaj Yadav
# 08/10/2024


# Change Control Log:

# Change #:1
# Changes Made : 1. import requests class and set it. Created static lookup dictionaries
#                2. Created class GetWeather and initiate, defined class setters and getters
#                3. define main and call to main
#                4. print outputs using pretty print
# Date of changes : 08/10/2024
# Author : Pankaj Yadav
# Change Approved by : Pankaj Yadav
# Date Moved to Production : 08/10/2024

# Import requests library
import requests

# Define static translate dictionaries
unit_lookup = {1: 'metric', 2: 'imperial', 3: 'standard'}
symbol_lookup = {1: '\u00b0C', 2: '\u00b0F', 3: '\u00b0K'}


# Define pretty print to print out final json data
def pretty_print(data, sym):
    """ This function creates a formatted output """

    if data:
        display_var = f"\nCurrent Weather lookout for the location : {data['name']}, {data['sys']['country']}"
        print("_" * len(display_var))
        print(display_var)
        print("-" * len(display_var))
        print(f"Current Temperature     : {round(data['main']['temp'])}{sym}")
        print(f"Feels Like              : {round(data['main']['feels_like'])}{sym}")
        print(f"Minimum Temperature     : {round(data['main']['temp_min'])}{sym}")
        print(f"Maximum Temperature     : {round(data['main']['temp_max'])}{sym}")
        print(f"Pressure                : {data['main']['pressure']}hPa")
        print(f"Humidity                : {data['main']['humidity']}%")

        # If it rains add rain parameters
        if data['weather'][0]['main'] == 'Rain':
            print(f"Cloud Cover             : {data['clouds']['all']}%")
            print(f"Rain in 1 Hr            : {data['rain']['1h']}mm")

        # Same for snow
        elif data['weather'][0]['main'] == 'Snow':
            print(f"Snow in 1 Hr            : {data['snow']['1h']}mm")
        print(f"Weather                 : {data['weather'][0]['description'].capitalize()}")


def requests_get_request(payload):
    """ This function requests the URI and returns the response """

    try:
        # Get request
        response = requests.get(payload, timeout=(5, 10))

        # raise HTTPError if occurred
        response.raise_for_status()

        # return the response back
        return response.json()

    # Exception handling
    except requests.HTTPError as http_error:
        print(f"There was an HTTP error. Try again! \n Description : {http_error}")
        restart()
    except requests.ConnectionError as connection_error:
        print(f"There was an connection error. Try again! \n Description : {connection_error}")
        restart()
    except requests.RequestException as request_error:
        print(f"There was a RequestException error. Try again! \n Description : {request_error}")
        restart()
    except TypeError as type_error:
        print(f"There was a Type_Error Exception. Try again! \n Description : {type_error}")
        restart()
    except Exception as err:
        print(f"Other error occurred: {err}")
        restart()


# Define class
class GetWeather:
    """ This class brings in api key and creates payload based on user inputs"""

    # initializing class object
    def __init__(self, apikey):
        self.apikey = apikey

    def get_weather_by_city(self, city, state, country, unit_type):
        """ This function creates a payload based on city and state and country"""

        geo_var = f"q={city},{state},{country}"
        payload = f"https://api.openweathermap.org/data/2.5/weather?{geo_var}&appid={self.apikey}&units={unit_type}"

        # Calls requests_get_request function and return the response
        return requests_get_request(payload)

    def get_weather_by_zip(self, zipcd, country, unit_type):
        """ This function creates a payload based on zip and country """

        # Calls get lat long function to provide coordinates
        lat_long = self.get_lat_long(zipcd, country)

        coord = f"lat={lat_long['lat']}&lon={lat_long['lon']}"
        payload = f"https://api.openweathermap.org/data/2.5/weather?{coord}&appid={self.apikey}&units={unit_type}"

        # Calls requests_get_request function and return the response
        return requests_get_request(payload)

    def get_lat_long(self, zipcd, country):
        """ This function returns lat long based on zip and country """
        payload = f"https://api.openweathermap.org/geo/1.0/zip?zip={zipcd},{country}&appid={self.apikey}"
        return requests_get_request(payload)






def restart():
    """ restarts the program in case of exception and let user decide what to do"""

    print("\nThere was an exception in last call Restarting the program...")
    main()


def variable_validation(invar, vartype):
    """ This function checks if the variable is valid or not"""

    while True:  # repeats unless all conditions met
        temp_var = input(invar)

        # for numeric data
        if vartype.upper() == 'INT' or vartype.upper == 'FLOAT':
            try:
                if len(temp_var) != 0 and int(temp_var) != 0 or temp_var.isdigit():
                    break
            except ValueError:
                print('Please enter an integer')
                continue

        # string validation
        elif vartype.upper() == 'STR':
            try:
                if len(temp_var) != 0 or temp_var != "":
                    break

            except ValueError:
                print('Please enter an integer str except')
                continue

        else:
            print("Please enter a valid value else")
            continue

    return temp_var


def user_input_city_zip():
    """ This function creates a city or zipcode choice variable from user input """

    while True:  # repeats unless one of the two is chosen

        city_zip_choice = (
            variable_validation("""Would you like to lookup weather by
                                 \n(1) City/state \n(2) Zipcode:""",
                                'int'))
        # try - except to take care of gibberish
        try:
            if int(city_zip_choice) in [1, 2]:
                break
            else:
                print("Please enter a valid choice: 1 or 2")

        except ValueError:
            print("Please enter a valid choice: 1 or 2")

    return int(city_zip_choice)


def user_input_unit():
    """ This function creates variable to choose unit from user input """

    while True:  # repeats unless one of the two is chosen
        unit_type_choice = (
            variable_validation('Enter the choice of units \n (1) Celsius, (2) Fahrenheit, (3) Kelvin :',
                                'int'))

        # try - except to take care of gibberish
        try:
            if int(unit_type_choice) in [1, 2, 3]:
                break

            else:
                print("Please enter a valid choice between 1, 2 & 3")

        except ValueError:
            print("Please enter a valid choice between 1, 2 & 3")

    return int(unit_type_choice)


def check_geo_codes(check_var,type):
    if type == 'cd':
       while True:

           val_var = variable_validation(check_var, 'str').upper()
           try:
              if len(val_var) != 0 and val_var != "" and len(val_var) <= 2:
                  break

           except ValueError:
               print('Please enter an integer str except')
               continue

       return val_var


def get_city(apikey,city):

    payload = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=20&appid={apikey}"
    response = requests.get(payload)
    data = response.json()
    if data:
        for city in data:
           print(city)
        return data
    else:
        print('City not found')
        return None

def main():
    """ main function """

    print("\nWelcome to Weather App!! Please choose your options!  \n")

    apikey = '2c1b35e5440bdc65acf4033a0c624302'

    while True:
        city_zip_choice = user_input_city_zip()  # zip vs cit state choice
        unit_type_choice = user_input_unit()  # C, F or K
        unit_type = unit_lookup[unit_type_choice]
        symb_type = symbol_lookup[unit_type_choice]
        temp = GetWeather(apikey)

        if city_zip_choice == 1:  # city/state

            city = variable_validation('Provide full name of your city: ', 'str').capitalize()

            state = check_geo_codes('Provide 2 digit state code (e.g. TX, NE, CA etc.): ','cd')

            country = check_geo_codes('Provide 2 digit country code (e.g. US,Canada-CA IN MX: ','cd')

            weather_data = temp.get_weather_by_city(city, state, country, unit_type)

            pretty_print(weather_data, symb_type)

        elif city_zip_choice == 2:  # Zipcode
            # Postal zipcodes could be alphanumeric hence just made sure it is not empty, the user should know the
            # correct zip code of city
            zipcd = variable_validation('Provide zipcode of your city: ', 'str').upper()

            country = check_geo_codes('Provide 2 digit country code (e.g. US,Canada-CA IN MX: ','cd')

            weather_data = temp.get_weather_by_zip(zipcd, country, unit_type)

            pretty_print(weather_data, symb_type)

        else:
            print("Kindly enter a valid choice!")

        get_more_weather = input("\nWould you like to check weather for more cities? Type (yes) or (no):").upper()

        if get_more_weather != "YES":
            print("Thank you for using the Weather app!")
            break


# call to main
if __name__ == "__main__":
    main()
