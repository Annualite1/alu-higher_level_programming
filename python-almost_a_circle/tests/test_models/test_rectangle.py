#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_init_basic(self):
        """Test basic instantiation."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_init_with_id(self):
        """Test instantiation with an explicit id."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_type_error(self):
        """Test TypeError on non-integer width."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_value_error(self):
        """Test ValueError on width <= 0."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as e:
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_type_error(self):
        """Test TypeError on non-integer x."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as e:
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_value_error(self):
        """Test ValueError on y < 0."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(d, expected)


if __name__ == "__main__":
    unittest.main()
