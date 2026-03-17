import unittest
from digin import NestedDict, NestedTuple


class TestNestedTuple(unittest.TestCase):
    def setUp(self):
        self.data = ({"a": (1, 2, 3)}, {"b": (4, 5, 6)})
        self.nested_tuple = NestedTuple(self.data, ".")

    def test_get(self):
        inner = self.nested_tuple.get("0")
        self.assertIsInstance(inner, NestedDict)
        self.assertEqual(self.nested_tuple.get("0.a.1"), 2)
        self.assertEqual(self.nested_tuple.get("1.b.0"), 4)

    def test_getitem(self):
        item = self.nested_tuple[0]
        self.assertEqual(item, {"a": (1, 2, 3)})
        item_wrapped = self.nested_tuple[[0]]
        self.assertIsInstance(item_wrapped, NestedDict)

    def test_call_read(self):
        self.assertEqual(self.nested_tuple("0.a.2"), 3)
        self.assertEqual(self.nested_tuple("1.b.2"), 6)

    def test_nested_tuple_wraps_inner_tuple(self):
        inner_tuple = self.nested_tuple.get("0.a")
        self.assertIsInstance(inner_tuple, NestedTuple)


if __name__ == '__main__':
    unittest.main()
