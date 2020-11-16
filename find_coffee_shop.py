import csv
import urllib3
import argparse
import sys
from scipy.spatial import distance
from collections import namedtuple

NearbyShop = namedtuple("NearbyShop", "name distance")


def get_closest_coffee_shops(my_location, locations, number_of_locations=3):
    """
    Find out the closest 3 locations from your location.
    :param my_location: is a tuple of 2 floats representing the x and y coordinates
    :param locations: is a tuple of a string and 2 floats, representing the name of the location and the x and y coordinates
    :return: the closest 3 locations and a list of issues discovered by parsing the data
    """
    shops = []
    issues = []
    for row_num, data in enumerate(locations, 1):
        try:
            name, x_str, y_str = data
            x = float(x_str)
            y = float(y_str)
            dist = round(distance.euclidean(my_location, [x, y]), 4)
            shops.append(NearbyShop(name, dist))
        except ValueError as ve:
            issues.append(f"Issue at row number {row_num}: {ve} ")
    shops.sort(key=lambda shop: shop.distance)
    return shops[:number_of_locations], issues


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float, help="Provide the user x coordinate")
    parser.add_argument("y", type=float, help="Provide the user y coordinate")
    parser.add_argument("shops_url", type=str, help="Provide the shop data url")
    args = parser.parse_args()

    my_loc = [args.x, args.y]

    http = urllib3.PoolManager()
    response = http.request('GET', args.shops_url)
    if response.status != 200:  # checking for the OK status
        print(f"The URL you provided generated a code {response.status}: {response.reason}", file=sys.stderr)
        exit()

    cr = csv.reader(response.data.decode('utf-8').split("\n"))
    coffee_shops = list(cr)
    coffee_shops, found_issues = get_closest_coffee_shops(my_loc, coffee_shops)

    for err in found_issues:
        print(err, file=sys.stderr)

    for shop in coffee_shops:
        print(f"{shop.name},{shop.distance}")
