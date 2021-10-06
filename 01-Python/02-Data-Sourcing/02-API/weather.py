# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    query = query.lower()
    response = requests.get(
        f"https://www.metaweather.com/api/location/search/?query={query}"
    ).json()
    if len(response) != 0:
        return (response[0])
    else:
        return None


def weather_forecast(woeid):
    responses2 = requests.get(
        f"https://www.metaweather.com/api/location/{woeid}/").json()
    city = responses2["title"]
    #print(f"Here's the weather in {city}")
    liste_weather = []
    for i in range(0, 6):
        liste_weather.append(responses2["consolidated_weather"][i])

    return liste_weather


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
