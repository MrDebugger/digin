import unittest
from digin import NestedDict


class TestDefaultDelimiter(unittest.TestCase):
    def setUp(self):
        self.data = {"x": {"y": {"z": 42}}, "items": [10, 20, 30]}
        self.nd = NestedDict(self.data)

    def test_get_with_default_delimiter(self):
        self.assertEqual(self.nd.get("x->y->z"), 42)

    def test_getitem_with_default_delimiter(self):
        self.assertEqual(self.nd["x->y->z"], 42)

    def test_call_get_with_default_delimiter(self):
        self.assertEqual(self.nd("x->y->z"), 42)

    def test_call_set_with_default_delimiter(self):
        self.nd("x->y->z", 99)
        self.assertEqual(self.nd("x->y->z"), 99)

    def test_list_access_with_default_delimiter(self):
        self.assertEqual(self.nd("items->1"), 20)

    def test_repr_contains_default_delimiter(self):
        r = repr(self.nd)
        self.assertIn("->", r)


if __name__ == '__main__':
    unittest.main()
