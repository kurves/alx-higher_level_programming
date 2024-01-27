#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test fo max integer function
    """
    def test_positive_numbers(self):
       """
       Tests finding the maximum
       """
       self.assertEqual(max_integer([1, 7, 4, 10]), 10)

   def test_negative_numbers(self):
       """
       Tests finding the maximum
       """
       self.assertEqual(max_integer([-6, -2, -7, -1]), -1)

   def test_mixed_numbers(self):
       """
       Tests finding the maximu
       """
       self.assertEqual(max_integer([-5, 4, -7, 20, -1]), 20)

   def test_empty_list(self):
       """
       Tests finding the maximum in an empty list.
       """
       self.assertEqual(max_integer([]), None)

   def test_single_element_list(self):
       """Tests finding the maximum in a list with a single element."""
       self.assertEqual(max_integer([9]), 9)
       self.assertEqual(max_integer([-4]), -4)

   def test_non_integer_values(self):
       """Tests handling lists with non-integer values.
       """
       with self.assertRaises(TypeError):
           max_integer([2, 9, "lorry"])
       with self.assertRaises(TypeError):
           max_integer([5.9, 0, 6])

if __name__ == '__main__':
   unittest.main()

