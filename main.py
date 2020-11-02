import json
import math
import requests
from bs4 import BeautifulSoup


def get_distance(loc1, loc2):
    return round(math.sqrt((loc1[0] - loc2[0]) * (loc1[0] - loc2[0]) + (loc1[1] - loc2[1]) * (loc1[1] - loc2[1])), 4)


#  extra idea for the future - use this to get your location live

# send_url = "http://api.ipstack.com/check?access_key=da96285c376c412b6bab56d3dfaa4961"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# my_location = [float(geo_json['latitude']), float(geo_json['longitude'])]


my_location = [0, 0]
page = requests.get("https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv")
soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)
coffee_shops = []
locations = str(soup).split('\n')
shortest_distance = math.inf
for loc in locations:
    data = str(loc).split(",")
    dist = get_distance(my_location, [float(data[1]), float(data[2])])
    coffee_shops.append([data[0], float(data[1]), float(data[2]), dist])

print(coffee_shops)
# coffee_shops = coffee_shops[coffee_shops[:, 3].argsort()]
# print(coffee_shops)
