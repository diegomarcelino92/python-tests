import unittest
from unittest.mock import patch

import requests
from cake import CakeRecipe


class TestCake(unittest.TestCase):

    def setUp(self) -> None:
        self.cake = CakeRecipe()
        return super().setUp()

    def test_cake_should_have_ingredients(self):
        self.cake.add_ingredient('flour')
        self.cake.add_ingredient('sugar')
        self.cake.add_ingredient('eggs')

        self.assertEqual(self.cake.ingredients, ['flour', 'sugar', 'eggs'])

    def test_cake_should_roast(self):
        with patch.object(requests, 'get') as mock_get:
            mock_get.return_value.ok = True

            self.assertEqual(self.cake.roast(), 'Roasted')

    def test_cake_should_not_roast(self):
        with patch.object(requests, 'get') as mock_get:
            mock_get.return_value.ok = False

            self.assertEqual(self.cake.roast(), 'Not Roasted')


if __name__ == '__main__':
    unittest.main(verbosity=2)
