
from app.restaurant import fetch_restaurant_data


def test_restaurant_data(c_zipcode="10003"):

    data = fetch_restaurant_data(c_zipcode)

    # it returns a list:
    assert isinstance(data, list)