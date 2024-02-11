
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        expected = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(Base.to_json_string(data), expected)


if __name__ == '__main__':
    unittest.main()
