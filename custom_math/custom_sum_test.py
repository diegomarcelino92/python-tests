import unittest

from custom_sum import custom_sum


class TestSum(unittest.TestCase):
    def test_sum_positive_number(self):
        result = custom_sum(5, 10)
        self.assertEqual(result, 15)

    def test_sum_negative_number(self):
        result = custom_sum(-5, 10)
        self.assertEqual(result, 5)

    def test_sum_multiples_values(self):
        entries = (
            (5, 10, 15),
            (-5, 10, 5),
            (-5, 5, 0)
        )

        for entrie in entries:
            with self.subTest(entrie=entrie):
                num1, num2, expect_result = entrie
                result = custom_sum(num1, num2)
                self.assertEqual(expect_result, result)


unittest.main(verbosity=2)
