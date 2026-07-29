#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ascending ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test with no argument given."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-1, 5, 3, -10]), 5)

    def test_duplicate_max(self):
        """Test with duplicate maximum values."""
        self.assertEqual(max_integer([4, 4, 2, 4]), 4)

    def test_all_same(self):
        """Test with all elements the same."""
        self.assertEqual(max_integer([7, 7, 7]), 7)


if __name__ == "__main__":
    unittest.main()
