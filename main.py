import math
import csv
import requests
from bs4 import BeautifulSoup
import sys


def get_distance(loc1, loc2):
    return round(math.sqrt((loc1[0] - loc2[0]) * (loc1[0] - loc2[0]) + (loc1[1] - loc2[1]) * (loc1[1] - loc2[1])), 4)


def bye(message):
    print(message)
    quit()


#  extra idea for the future - use this to get your location live

# send_url = "http://api.ipstack.com/check?access_key=da96285c376c412b6bab56d3dfaa4961"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# my_location = [float(geo_json['latitude']), float(geo_json['longitude'])]

if not (len(sys.argv) > 2 and (type(sys.argv[1]) == int or float) and (type(sys.argv[2]) == int or float)):
    bye("In order to proceed please provide arguments for this call having the following order: \n "
        "<user x coordinate> <user y coordinate> <shop data url>")

my_location = [float(sys.argv[1]), float(sys.argv[2])]
try:
    page = requests.get(sys.argv[3])
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    locations = str(soup).split('\n')
    # print(locations)
except:
    bye("In order to proceed please provide arguments for this call having the following order: \n "
        "<user x coordinate> <user y coordinate> <shop data url>")

# print(soup)
coffee_shops = []
for loc in locations:
    data = str(loc).split(",")
    if not (len(data) == 3 and (type(data[1]) == int or float) and (type(data[2]) == int or float)):
        bye("The provided data needs to have the following format: \n"
            "<coffee shop name>,<shop x coordinate>,<shop y coordinate>")
    dist = get_distance(my_location, [float(data[1]), float(data[2])])
    coffee_shops.append([data[0], float(data[1]), float(data[2]), dist])
coffee_shops.sort(key=lambda x: x[3])

for i in range(3):
    if not coffee_shops[i]:
        break
    print(coffee_shops[i][0] + "," + str(coffee_shops[i][3]))
