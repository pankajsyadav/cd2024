# Weather APIs from openweathermap.org:
# Default : 2c1b35e5440bdc65acf4033a0c624302
# city_weather_api : 2b15b0d74fa735aae5c3bc1daf0a7710

import requests
country = input("Enter a country name: ")
rcc = requests.get(f'https://iso3166-2-api.vercel.app/api/country_name/{country}')
get_country = rcc.json()
print(get_country)
