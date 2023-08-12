import os
from dotenv import load_dotenv
import requests
import json
from pprint import pprint


load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

API_KEY = os.getenv("API_KEY")


def fetch_restaurant_data(c_zipcode):
    request_url = "https://api.yelp.com/v3/businesses/search"
    
    request_params = {
        'term': 'food',
        'limit': 50,
        'offset': 0,  # Reset offset to 0 for each request
        'radius': 10000,
        'location': 'new york'
    }
    request_headers = {'Authorization': f"Bearer {API_KEY}"}

    response = requests.get(url=request_url, params=request_params, headers=request_headers)

    #chatgpt wrapped the code into an if else statement & cleaned up the "businesses" key in the fetching instead of filtering after
    if response.status_code == 200:
        restaurant_data = response.json()
        restaurants = restaurant_data.get("businesses", [])
        restaurants = [r for r in restaurants if r.get("rating", 0) >= 4.5]
        restaurants = [r for r in restaurants if c_zipcode == r["location"].get("zip_code", "")]
        return restaurants
    else:
        print("Error while fetching restaurant data:", response.status_code)
        return []



if __name__ == "__main__":
    
    c_zipcode = input ("What's your zipcode '10001', '10003', '11222' ? ")

    restaurant = fetch_restaurant_data(c_zipcode)

    zipcode_list = [ r["location"]["zip_code"] for r in restaurant ]

    if c_zipcode in zipcode_list:

        print("RESTAURANT REPORT...")

        for r in restaurant:
            print (r["name"], "|", r["location"]["address1"]+", "+r["location"]["city"]+", "+r["location"]["zip_code"])
    
    else:
        print ("OOPS! Invalid input. Try again.")


