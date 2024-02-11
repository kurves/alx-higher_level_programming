import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5, 1, 2, 3)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 3)

    def test_size_validity(self):
        with self.assertRaises(TypeError):
            Square("5", 1, 2)
        with self.assertRaises(ValueError):
            Square(0, 1, 2)

    def test_size_property(self):
        square = Square(3)
        self.assertEqual(square.size, 3)

    def test_size_setter(self):
        square = Square(3)
        square.size = 5
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_str(self):
        square = Square(4, 2, 1, 42)
        self.assertEqual(str(square), "[Square] (42) 2/1 - 4")

    def test_update(self):
        square = Square(1, 1, 1, 1)
        square.update(10, 5, 5, 5)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        square = Square(3, 4, 5, 7)
        expected_dict = {'id': 7, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
