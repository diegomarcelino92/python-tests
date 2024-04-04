from unittest import TestCase, main

from eggs_with_bacon import eggs_with_bacon


class TestEggsWithBacos(TestCase):
    def test_eggs_with_bacon_should_accept_int_in_bacon_and_eggs_count(self):
        with self.assertRaises(AssertionError):
            eggs_with_bacon('1', '2')

    def test_eggs_with_bacon_should_return_empty_recipe(self):
        self.assertEqual(eggs_with_bacon(0, 0), 'empty')

    def test_eggs_with_bacon_should_return_eggs_recipe(self):
        self.assertEqual(eggs_with_bacon(1, 0), 'eggs')

    def test_eggs_with_bacon_should_return_bacon_recipe(self):
        self.assertEqual(eggs_with_bacon(0, 1), 'bacon')

    def test_eggs_with_bacon_should_return_bacon_with_eggs_recipe(self):
        self.assertEqual(eggs_with_bacon(1, 1), 'bacon with eggs')


if __name__ == '__main__':
    main(verbosity=2)
