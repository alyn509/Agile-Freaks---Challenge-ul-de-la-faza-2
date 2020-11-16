import unittest
import find_coffee_shop
from find_coffee_shop import NearbyShop


class TestFindCoffeeShop(unittest.TestCase):

    def test_get_coffee_shops(self):
        my_loc = [0, 0]
        coffee_shops = [['Loc 1', '1', '1'],
                        ['Loc 2', '2', '2'],
                        ['Loc 3', '3', '3'],
                        ['Loc 4', '4', '4'],
                        ['Loc 5', '5', '5'],
                        ['Loc 6', '6', '6']]
        expected_response = [NearbyShop(name='Loc 1', distance=1.4142),
                             NearbyShop(name='Loc 2', distance=2.8284),
                             NearbyShop(name='Loc 3', distance=4.2426)]
        expected_issues = []
        self.assertEqual(find_coffee_shop.get_closest_coffee_shops(my_loc, coffee_shops), (expected_response, expected_issues))

    def test_get_coffee_shops_fail(self):
        my_loc = [0, 0]
        coffee_shops = [['Loc 1', '1', '1'],
                        ['Loc 2', '2', '2'],
                        ['Loc 3', '3', 'cartof'],
                        ['Loc 4', '4'],
                        [],
                        ['Loc 5', '5', '5']]
        expected_response = [NearbyShop(name='Loc 1', distance=1.4142),
                             NearbyShop(name='Loc 2', distance=2.8284),
                             NearbyShop(name='Loc 5', distance=7.0711)]
        expected_issues = ["Issue at row number 3: could not convert string to float: 'cartof' ",
                           'Issue at row number 4: not enough values to unpack (expected 3, got 2) ',
                           'Issue at row number 5: not enough values to unpack (expected 3, got 0) ']
        self.assertEqual(find_coffee_shop.get_closest_coffee_shops(my_loc, coffee_shops), (expected_response, expected_issues))


if __name__ == '__main__':
    unittest.main()
