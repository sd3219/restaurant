
from app.restaurant import fetch_restaurant_data

#test
x = "string"
assert len(x) == 5

#def test_restaurant_data(c_zipcode="10003"):
#
#    data = fetch_restaurant_data(c_zipcode)
#
#    # it returns a list of dicts:
#    assert isinstance(data, list)
#    assert isinstance(data[0], dict)
#
#    # where each has the keys:
#    # "id"
#    # "alias"
#    # "name"
#    # "image_url"
#    # "is_closed"
#    # "url"
#    # "review_count"
#    # "categories"
#    # "rating"
#    # "coordinates"
#    # "transactions"
#    # "price"
#    # "location"
#    # "phone"
#    # "display_phone"
#    # "distance"
#    assert list(data[0].keys()) == ["id", "alias", "name", "image_url", "is_closed", "url", "review_count", "categories", "rating", "coordinates", "transactions", "price", "location", "phone", "display_phone", "distance"]