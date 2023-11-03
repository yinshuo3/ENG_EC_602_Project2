#!/usr/bin/env python3
import requests
import json
import googlemaps


def store_location():
    # Replace with your own Google Maps API key
    api_key = 'AIzaSyB7lsicgUpRD6WQsLRx2dVP2bUBFD6Y-SE'

    #this does work
    gmaps = googlemaps.Client(key='AIzaSyB7lsicgUpRD6WQsLRx2dVP2bUBFD6Y-SE')
    loc = gmaps.geolocate()

    lat = loc['location']['lat']
    #print(lat)
    lng = loc['location']['lng']

    # URL for the Google Geocoding API
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}'

    # Make a request to the Geocoding API to get the current location
    response = requests.get(url)

    data = response.json()

    #print('here')

    if data['status'] == 'OK':
        results = data['results']

        #print(results)
        if results:
            
            gps_coordinate_list.append((lat, lng))
            street_address_list.append(results[0]["formatted_address"])

        else:
            print("No results found.")
    else:
        print(f"Geocoding API request failed with status: {data['status']}")


if __name__ == '__main__':
    street_address_list = []

    gps_coordinate_list = []
    while True:
        cmd_str = input("Please type in command: ")

        if cmd_str == "here":
            store_location()

        elif cmd_str == "quit":
            break
        
        else:
            print("command not recognized")
            continue

    print(street_address_list)
    print(gps_coordinate_list)
