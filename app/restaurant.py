import os
from dotenv import load_dotenv
import requests
import json
from pprint import pprint


load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

API_KEY = os.getenv("API_KEY")


def fetch_restaurant_data(zip_code):
    request_url = "https://api.yelp.com/v3/businesses/search"

    request_params = {
    'term': 'food',
    'limit': 50,
    'offset': 50,
    'radius': 10000,
    'location': 'new york'
    }
    request_headers = {'Authorization': f"bearer {API_KEY}"}

    response = requests.get(url=request_url, params=request_params, headers=request_headers)
    restaurant = json.loads(response.text)
    restaurant = restaurant["businesses"]
    restaurant = [ r for r in restaurant if r["rating"] >= 4.5 ]

    return restaurant




if __name__ == "__main__":

    print("RESTAURANT REPORT...")

    c_zipcode = input ("What's your zipcode '10001', '10003', '11222' ? ")
    
    restaurant = fetch_restaurant_data(c_zipcode)

    for r in restaurant:
        if c_zipcode == r["location"]["zip_code"]:
            print (r["name"])


