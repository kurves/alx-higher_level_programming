import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(10, 20, 1, 2, 3)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 3)

    def test_width_validity(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 20, 1, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 1, 2)

    def test_height_validity(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "20", 1, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 1, 2)

    def test_x_validity(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "1", 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1, 2)

    def test_y_validity(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 1, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 1, -2)

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_str(self):
        rect = Rectangle(4, 8, 2, 1, 42)
        self.assertEqual(str(rect), "[Rectangle] (42) 2/1 - 4/8")

    def test_update(self):
        rect = Rectangle(1, 1, 1, 1)
        rect.update(10, 5, 5, 5, 5)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_to_dictionary(self):
        rect = Rectangle(3, 4, 5, 6, 7)
        expected_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
